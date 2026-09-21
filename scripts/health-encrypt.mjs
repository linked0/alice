#!/usr/bin/env node
// Encrypt the health Life tiles (jay, 2026-09-18).
//
//   HEALTH_PASS='…' node scripts/health-encrypt.mjs ~/Documents/Private/life-health-rules.md
//
// Why encryption and not a hashed password: a hash only lets the page check the password; the text
// would still be readable in the HTML source and in git. Here the plaintext never enters the repo.
// The markdown is split into tiles (one per `## ` heading, with `### en` / `### ko` blocks), the whole
// bundle is encrypted with AES-256-GCM under a key derived from the password with PBKDF2-SHA256
// (600k iterations, random salt). Since 2026-09-21 the ciphertext goes to the Firestore document
// health/bundle and the repo keeps only the labels in docs/topics/_health.js; the page fetches the
// bundle after Google sign-in and derives the same key in the browser (WebCrypto) to decrypt.
// Why both layers: publishing the ciphertext used to mean anyone could copy it once and brute-force
// the password offline forever. Behind sign-in they cannot copy it. Encryption stays anyway because
// security rules govern browsers, not service accounts, and this project has ones with project-wide
// access. Sign-in decides who may FETCH the bytes; the password decides who may READ them.
// The limit is still the password, and there is no reset: lose the passphrase and the text is gone.
import fs from 'node:fs';
import path from 'node:path';
import { webcrypto } from 'node:crypto';
import { execFileSync } from 'node:child_process';
const { subtle } = webcrypto;

const src = process.argv[2];
const pass = process.env.HEALTH_PASS;
if (!src || !pass) { console.error('usage: HEALTH_PASS=… node scripts/health-encrypt.mjs <rules.md>'); process.exit(2); }
const md = fs.readFileSync(src, 'utf8');

// parse tiles
const tiles = [];
for (const block of md.split(/^## /m).slice(1)) {
  const [head, ...rest] = block.split('\n');
  const body = rest.join('\n');
  const en = (body.match(/### en\s*\n([\s\S]*?)(?=\n### |\s*$)/) || [, ''])[1].trim();
  const ko = (body.match(/### ko\s*\n([\s\S]*?)(?=\n### |\s*$)/) || [, ''])[1].trim();
  const [label, ...titleParts] = head.split(' — ');
  tiles.push({ label: label.trim(), title: titleParts.join(' — ').trim(), en, ko });
}
if (!tiles.length) { console.error('no "## " tiles found'); process.exit(1); }

const enc = new TextEncoder();
const salt = webcrypto.getRandomValues(new Uint8Array(16));
const iv = webcrypto.getRandomValues(new Uint8Array(12));
const ITER = 600000;
const base = await subtle.importKey('raw', enc.encode(pass), 'PBKDF2', false, ['deriveKey']);
const key = await subtle.deriveKey({ name: 'PBKDF2', salt, iterations: ITER, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['encrypt']);
const plain = enc.encode(JSON.stringify(tiles));
const ct = new Uint8Array(await subtle.encrypt({ name: 'AES-GCM', iv }, key, plain));
const b64 = (u8) => Buffer.from(u8).toString('base64');
const labels = tiles.map((t) => t.label);
const bundle = { v: 1, kdf: 'PBKDF2-SHA256', iter: ITER, salt: b64(salt), iv: b64(iv), ct: b64(ct), tiles: labels };

// The ciphertext goes to Firestore, not into this repo (jay, 2026-09-21). The repo keeps only the
// labels, which are "Health 1", "Health 2" … and say nothing. Encryption stays on top of the
// database rather than instead of it: security rules govern browsers, not service accounts, and this
// project has ones with project-wide access — so sign-in decides who may fetch the bytes and the
// password decides who may read them.
const PROJECT = 'doubletree-498007';
const token = execFileSync('gcloud', ['auth', 'print-access-token'], { encoding: 'utf8' }).trim();
const fields = {
  v: { integerValue: String(bundle.v) }, kdf: { stringValue: bundle.kdf },
  iter: { integerValue: String(bundle.iter) }, salt: { stringValue: bundle.salt },
  iv: { stringValue: bundle.iv }, ct: { stringValue: bundle.ct },
  tiles: { arrayValue: { values: labels.map((l) => ({ stringValue: l })) } },
};
const url = `https://firestore.googleapis.com/v1/projects/${PROJECT}/databases/(default)/documents/health/bundle`;
const res = await fetch(url, {
  method: 'PATCH',
  headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ fields }),
});
if (!res.ok) throw new Error(`Firestore write failed: ${res.status} ${await res.text()}`);

const dest = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'docs', 'topics', '_health.js');
fs.writeFileSync(dest, `window.__HEALTH__=${JSON.stringify({ v: 1, remote: 'firestore', tiles: labels })};\n`);
console.log(`${tiles.length} tiles encrypted (${ct.length} bytes) \u2192 Firestore health/bundle; labels only \u2192 ${path.relative(process.cwd(), dest)}`);
// The locked Life cards (numbered 1000, 999 …) follow the tile list; regenerate them after every encryption.
execFileSync('python3', [path.join(path.dirname(new URL(import.meta.url).pathname), 'health-cards.py')], { stdio: 'inherit' });
