#!/usr/bin/env node
// Encrypt the health Life tiles (jay, 2026-09-18).
//
//   HEALTH_PASS='…' node scripts/health-encrypt.mjs ~/Documents/Private/life-health-rules.md
//
// Why encryption and not a hashed password: a hash only lets the page check the password; the text
// would still be readable in the HTML source and in git. Here the plaintext never enters the repo.
// The markdown is split into tiles (one per `## ` heading, with `### en` / `### ko` blocks), the whole
// bundle is encrypted with AES-256-GCM under a key derived from the password with PBKDF2-SHA256
// (600k iterations, random salt), and only {salt, iv, ciphertext, tiles: [labels]} is written to
// docs/topics/_health.js. notes.html derives the same key in the browser (WebCrypto) and decrypts.
// The limit is the password: a short dictionary-like one can be brute-forced offline by someone
// who copies the file, so prefer a long passphrase; re-run this script to change it.
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
const out = { v: 1, kdf: 'PBKDF2-SHA256', iter: ITER, salt: b64(salt), iv: b64(iv), ct: b64(ct), tiles: tiles.map((t) => t.label) };
const dest = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'docs', 'topics', '_health.js');
fs.writeFileSync(dest, `window.__HEALTH__=${JSON.stringify(out)};\n`);
console.log(`${tiles.length} tiles encrypted → ${path.relative(process.cwd(), dest)} (${ct.length} bytes)`);
// The locked Life cards (numbered 1000, 999 …) follow the tile list; regenerate them after every encryption.
execFileSync('python3', [path.join(path.dirname(new URL(import.meta.url).pathname), 'health-cards.py')], { stdio: 'inherit' });
