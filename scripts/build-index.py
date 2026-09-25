#!/usr/bin/env python3
"""Build the machine-readable index of Knowledge Notes (jay, 2026-09-21: "Let the system hold the index").

Karpathy's LLM-wiki pattern (Tech #109; applied in the learning-greed item) has raw sources, a wiki, a schema,
a log and an index. Knowledge Notes had the wiki (docs/topics/*.html), the schema (docs/topics/README.md) and
the log (docs/history/). This script writes the index, one line per item, so "have I already learned this"
is answered by a search (scripts/notes-search.py) instead of by memory:

  docs/topics/index.json   every field, for scripts and for the model
  docs/topics/index.md     one table row per item, for grep and for reading

Sources of truth, read only (nothing here is edited): docs/topics/_nav.js (order, number, status, title),
each detail page's kicker (type, added date, source, bin, raw link), its Korean <h1>, its English lead, the
"Sources:" paragraph (related item numbers), and docs/topics/vocab/<page>.md (key expressions). Health items
are listed by number only (LOCKED). Run by add-tech-item.py, english-notes.py, reorder-by-status.py and
roll-done-states.py after every change; safe to run alone. Idempotent.
"""
import json, re, pathlib, html, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
TOPICS = ROOT / "topics"
SECTION = {"nav-sec-blockchain": "Tech", "nav-sec-fundamentals": "Theory", "nav-sec-invest": "Invest", "nav-sec-english": "Eng", "nav-sec-mindset": "Life"}
KST = datetime.timezone(datetime.timedelta(hours=9))

def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def read_page(href):
    f = TOPICS / href
    if not f.exists(): return {}
    s = f.read_text()
    out = {}
    m = re.search(r'<p class="topic-kicker">(.*?)</p>', s, re.S)
    if m:
        k = m.group(1)
        spans = re.findall(r'<span([^>]*)>(.*?)</span>', k, re.S)
        for attrs, body in spans:
            t = re.search(r'title="([^"]+)"', attrs)
            if 'class="topic-no"' in attrs: continue
            if not t: out.setdefault("type", text(body)); continue
            if t.group(1) == "raw":
                a = re.search(r'href="([^"]+)"', body); out["raw"] = a.group(1) if a else text(body)
            elif t.group(1) in ("added", "source", "bin", "section"): out[{"added": "date"}.get(t.group(1), t.group(1))] = text(body)
    ko = s.find('<article id="ko"')
    if ko != -1:
        h = re.search(r"<h1>(.*?)</h1>", s[ko:], re.S)
        if h: out["title_ko"] = text(re.sub(r'<span class="badge".*?</span>', "", h.group(1), flags=re.S))
    en_start = s.find('<article id="en"'); en_end = ko if ko != -1 else len(s)
    en = s[en_start:en_end] if en_start != -1 else s
    lead = re.search(r'<p class="lead">(.*?)</p>', en, re.S)
    if lead:
        t = text(lead.group(1)); out["lead"] = t[:300] + ("…" if len(t) > 300 else "")
    src = re.search(r"<p>(?:(?!</p>).)*?(Sources?:.*?)</p>", en, re.S)   # "Sources:" may open the paragraph or sit at the end of the Verified paragraph
    if src:
        t = text(src.group(1))
        rel = set(re.findall(r"(?:Tech |Eng )#(\d+)", t)) | set(re.findall(r"(?<![#\d])#(\d+)", t)) | {f"{sec} {n}" for sec, n in re.findall(r"(Invest|Life|Theory|Eng) (\d{3,4})", t)}
        out["related"] = sorted(rel, key=lambda x: (len(x), x))[:40]
    return out

def vocab_for(href):
    f = TOPICS / "vocab" / (pathlib.Path(href).stem + ".md")
    if not f.exists(): return []
    rows = []
    for line in f.read_text().splitlines():
        if not line.startswith("|") or set(line.strip()) <= set("|-: "): continue
        cell = line.split("|")[1].strip()
        if cell in ("Expression", ""): continue
        rows.append(re.sub(r"[*`]", "", cell))
    return rows

nav = json.loads(re.match(r"window\.__NAV__=(.*);\s*$", (TOPICS / "_nav.js").read_text(), re.S).group(1))
items = []
for sec in nav["sections"]:
    name = SECTION[sec["navId"]]
    for pos, x in enumerate(sec["items"], 1):
        no = re.match(r'<span class="topic-no">(\d+)</span>', x["text"])
        tag = re.search(r'<span class="topic-tag"[^>]*>([^<]*)</span>', x["text"])
        row = {"no": int(no.group(1)) if no else None, "section": name, "key": x["key"], "href": x["href"], "status": x["label"], "position": pos,
               "title_en": text(re.sub(r'<span class="topic-(?:no|tag)">[^<]*</span>', "", x["text"]))}
        if tag: row["tag"] = tag.group(1)
        if x.get("done"): row["done"] = x["done"]
        if x["label"] == "LOCKED": row["title_en"] = row["title_en"] or f"Health {pos}"; items.append(row); continue
        row.update(read_page(x["href"]))
        v = vocab_for(x["href"])
        if v: row["vocab"] = v
        items.append(row)

now = datetime.datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")
counts = {s: sum(1 for i in items if i["section"] == s) for s in SECTION.values()}
done = sum(1 for i in items if i["status"] in ("DONE", "RECENTLY DONE", "REVISIT"))
(TOPICS / "index.json").write_text(json.dumps({"generated": now, "counts": counts, "done": done, "all": len(items), "items": items}, ensure_ascii=False, indent=0) + "\n")

def cell(v): return (v or "").replace("|", "\\|").replace("\n", " ")
lines = ["# Knowledge Notes — index", "",
         f"Generated {now} by `scripts/build-index.py` — do not edit; one line per item, every section. Machine copy: [`index.json`](index.json). "
         f"Search: `python3 scripts/notes-search.py <words>` answers \"have I already learned this\" before a new item is added. "
         f"Raw sources: [`raw/`](raw/README.md). Schema: [`README.md`](README.md).", "",
         "Counts: " + " · ".join(f"{s} {n}" for s, n in counts.items()) + f" · done {done}/{len(items)}", "",
         "| No | Section | Status | Added | Done | Type | Source | Bin | Title | 제목 | Key | Raw |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for i in items:
    raw = f"[raw]({i['raw']})" if i.get("raw") else ""
    lines.append(f"| {i['no']} | {i['section']}{' · ' + i['tag'] if i.get('tag') else ''} | {i['status']} | {cell(i.get('date'))} | {cell((i.get('done') or '')[:10])} | {cell(i.get('type'))} | {cell(i.get('source'))} | {cell(i.get('bin'))} | [{cell(i['title_en'])}]({i['href']}) | {cell(i.get('title_ko'))} | `{i['key']}` | {raw} |")
(TOPICS / "index.md").write_text("\n".join(lines) + "\n")
print(f"index: {len(items)} items ({done} done) → docs/topics/index.json, index.md; with raw {sum(1 for i in items if i.get('raw'))}, with bin {sum(1 for i in items if i.get('bin'))}")
