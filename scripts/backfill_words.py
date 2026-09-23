#!/usr/bin/env python3
"""Write a `## Words` table into every english-N.md (jay, 2026-09-23).

jay's correction, same day: "I meant new words as some advanced vocabularies like relocation, base
that is used for specific meaning or so, not phrases." So this takes **single words only**. A phrase
belongs in `## Expressions`, which every item already has; what `## Words` is for is the word you
cannot yet say.

jay again, same day: "advanced vocabularies and the words used as unusual" — two categories, and the
selector takes both:
  1. **a common word carrying an unusual sense.** For a `Word` item the title *is* that word, so the
     title bypasses the frequency filter entirely. This is how `base`, `poach`, `nerve` and `credit`
     get in: the item exists because of the sense, not because the word is rare.
  2. **advanced vocabulary.** Single words from the Expressions column whose **Zipf frequency is below
     3.8** — measured, not guessed. That line separates `salary` 4.36, `nerve` 4.19 and `apologize`
     4.16 from `scrutiny` 3.74, `remit` 3.09, `gaffe` 2.66 and `connive` 1.64. Rarest first.

Pronunciation is CMUdict (Carnegie Mellon, 126k entries), ARPAbet converted to IPA. A word CMUdict does
not hold is skipped, never approximated. CMUdict marks compounds such as `outside` with two primary
stresses, so all but the last are demoted; and syllable onsets are walked back only through clusters
that can legally begin an English syllable, since /ts/ cannot and `outside` is out-side.

Known limit, recorded rather than hidden: these rows are dictionary-derived, not hand-checked, and
CMUdict's primary stress sometimes differs from a learner's dictionary.
"""
import re, sys, pathlib, cmudict
from wordfreq import zipf_frequency

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
CMU = cmudict.dict()
ADVANCED = 3.8   # Zipf; above this a Korean learner at jay's level already has the word

ARPA = {"AA":"ɑ","AE":"æ","AH":"ʌ","AO":"ɔ","AW":"aʊ","AY":"aɪ","EH":"ɛ","ER":"ɝ","EY":"eɪ",
        "IH":"ɪ","IY":"i","OW":"oʊ","OY":"ɔɪ","UH":"ʊ","UW":"u",
        "B":"b","CH":"tʃ","D":"d","DH":"ð","F":"f","G":"ɡ","HH":"h","JH":"dʒ","K":"k","L":"l",
        "M":"m","N":"n","NG":"ŋ","P":"p","R":"r","S":"s","SH":"ʃ","T":"t","TH":"θ","V":"v",
        "W":"w","Y":"j","Z":"z","ZH":"ʒ"}
VOWELS = set("AA AE AH AO AW AY EH ER EY IH IY OW OY UH UW".split())
STOPS, LIQ = set("pbtdkɡ"), set("rlwj")

def legal_onset(c):
    if len(c) <= 1: return True
    if len(c) == 2:
        a, b = c
        return ((a in STOPS and b in LIQ) or (a == "f" and b in "rlj") or (a == "θ" and b in "rw")
                or (a == "ʃ" and b == "r") or (a == "s" and b in "ptkfmnlwj")
                or (a == "h" and b == "j") or (a in "mnv" and b == "j"))
    return len(c) == 3 and c[0] == "s" and c[1] in "ptk" and c[2] in "rlwj"

def ipa(phones):
    prim = [i for i, p in enumerate(phones) if p.endswith("1")]
    if len(prim) > 1:
        phones = [p[:-1] + "2" if i in prim[:-1] else p for i, p in enumerate(phones)]
    out = []
    nsyl = sum(1 for p in phones if p[:-1] in VOWELS or p in VOWELS)
    for ph in phones:
        base, stress = (ph[:-1], ph[-1]) if ph[-1].isdigit() else (ph, None)
        sym = ARPA.get(base)
        if sym is None: return None
        if base == "AH" and stress == "0": sym = "ə"
        if base == "ER" and stress == "0": sym = "ɚ"
        if stress in ("1", "2") and nsyl > 1:
            j = len(out)
            while j > 0 and out[j-1][1] not in VOWELS and legal_onset([x for x, _ in out[j-1:]]):
                j -= 1
            out.insert(j, ("ˈ" if stress == "1" else "ˌ", None))
        out.append((sym, base))
    return "".join(s for s, _ in out)

def look(w):
    e = CMU.get(w.lower())
    return (ipa(e[0]), sum(1 for p in e[0] if p[:-1] in VOWELS or p in VOWELS)) if e else (None, 0)

STOP = set("""a an the and or but so if then than that this these those there here it its is are was
were be been being am do does did done have has had having will would shall should can could may might
must not no nor of in on at to for from with without by about into over under again more most other
some such only own same very just too also as we you your yours they them their he she his her him i me
my mine one two three first next last new old good bad big small long short high low right left up down
out off back now today day week month year time thing things make makes made made take takes took get
gets got go goes went come comes came know knows knew think thinks thought say says said see sees saw
want wants like likes use uses used work works worked need needs look looks give gives put puts keep
keeps let lets ask asks tell tells find finds call calls try tries mean means show shows help helps
what when where which who whom whose why how all any both each few many much every other another""".split())

def clean(t): return re.sub(r"\*\*|`", "", t)

def title_words(text):
    """Only a `Word` item's title is itself the vocabulary. A Line or Article title is a sentence, and
    taking its first words gave rows like `But` and `she` (found 2026-09-23)."""
    head = text.split("\n")[0]
    m = re.match(r"# \d+ · ([^—]+) — (.+)", head)
    if not m or m.group(1).strip().lower() != "word": return []
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'-]{1,}", clean(m.group(2)))
            if w.lower() not in STOP]

def expr_rows(text):
    rows, insec = [], False
    for l in text.split("\n"):
        if l.startswith("## "):
            insec = l[3:].strip().lower() == "expressions"; continue
        if not insec or not l.strip().startswith("|"): continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 2 or set("".join(cells)) <= set("-: ") or cells[0].lower() in ("expression","word"):
            continue
        rows.append(cells)
    return rows

def gloss(cell):
    g = clean(cell).split(" — ")[0].split(" · ")[0].strip()
    return (g[:58] + "…") if len(g) > 60 else g

made, thin = 0, []
for p in sorted(ROOT.glob("english-*.md"), key=lambda q: int(re.search(r"(\d+)", q.name).group(1))):
    text = p.read_text()
    if "\n## Words" in text: continue
    rows = expr_rows(text)
    default_gloss = gloss(rows[0][1]) if rows else ""
    picked, seen = [], set()

    # 1. the item's own headword — always, however common
    for w in title_words(text):
        lw = w.lower()
        if lw in seen: continue
        i, _ = look(w)
        if not i: continue
        seen.add(lw); picked.append((w, i, default_gloss))
        if len(picked) >= 2: break

    # 2. advanced single words out of the expressions, hardest first
    cands = []
    for cells in rows:
        for tok in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", clean(cells[0])):
            lw = tok.lower()
            if lw in seen or lw in STOP: continue
            i, n = look(tok)
            if not i: continue
            z = zipf_frequency(lw, "en")
            # 0.0 means the list has never seen it; with CMUdict membership already required that is a
            # real and very rare word (catenative), not a typo.
            seen.add(lw); cands.append((z, tok, i, gloss(cells[1])))
    cands.sort(key=lambda c: c[0])
    hard = [c for c in cands if c[0] < ADVANCED]
    # Prefer genuinely advanced words. An item that has none — a plain everyday line — still gets its
    # own two hardest words rather than an empty section, because jay asked for every item to carry one.
    chosen = hard if hard else cands[:2]
    picked += [(t, i, g) for _, t, i, g in chosen[:6 - len(picked)]]

    if not picked: thin.append(p.name); continue
    block = "\n## Words\n" + "".join(f"| {w} | /{i}/ | {g} |\n" for w, i, g in picked)
    idx = text.index("\n## Expressions")
    p.write_text(text[:idx] + block + text[idx:])
    made += 1

print(f"wrote ## Words into {made} file(s)")
if thin: print(f"too thin ({len(thin)}): {', '.join(thin[:12])}{' …' if len(thin)>12 else ''}")
