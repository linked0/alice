#!/usr/bin/env python3
"""Back-fill a `## Words` table into every english-N.md that lacks one (jay, 2026-09-23:
"for all eng items i want the new words included").

Word choice is not invented: it comes from the item's own `## Expressions` table, which is already the
curated vocabulary for that conversation. Pronunciation comes from **CMUdict**, Carnegie Mellon's
pronouncing dictionary (126k entries), converted ARPAbet -> IPA. Nothing is guessed: a word CMUdict
does not have is skipped rather than approximated, and an item that yields fewer than two words is
left alone and reported, because a one-row table is worse than none.

Known limit, recorded rather than hidden: CMUdict's primary-stress marking occasionally differs from a
learner's dictionary (it gives a-COUNT-ability where Oxford gives accoun-ta-BIL-ity). These rows are
dictionary-derived, not hand-checked. Items written by hand from #399 on carry checked pronunciation.
"""
import re, sys, pathlib, cmudict

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
CMU = cmudict.dict()

ARPA = {"AA":"ɑ","AE":"æ","AH":"ʌ","AO":"ɔ","AW":"aʊ","AY":"aɪ","EH":"ɛ","ER":"ɝ","EY":"eɪ",
        "IH":"ɪ","IY":"i","OW":"oʊ","OY":"ɔɪ","UH":"ʊ","UW":"u",
        "B":"b","CH":"tʃ","D":"d","DH":"ð","F":"f","G":"ɡ","HH":"h","JH":"dʒ","K":"k","L":"l",
        "M":"m","N":"n","NG":"ŋ","P":"p","R":"r","S":"s","SH":"ʃ","T":"t","TH":"θ","V":"v",
        "W":"w","Y":"j","Z":"z","ZH":"ʒ"}
VOWELS = {"AA","AE","AH","AO","AW","AY","EH","ER","EY","IH","IY","OW","OY","UH","UW"}

STOPS = set("pbtdkɡ")
LIQ = set("rlwj")
def legal_onset(c):
    """Can this IPA consonant cluster begin an English syllable? Conservative on purpose."""
    if len(c) <= 1: return True
    if len(c) == 2:
        a, b = c
        if a in STOPS and b in LIQ: return True
        if a == "f" and b in "rlj": return True
        if a in ("θ",) and b in "rw": return True
        if a == "ʃ" and b == "r": return True
        if a == "s" and b in "ptkfmnlwj": return True
        if a == "h" and b == "j": return True
        if a in ("m", "n") and b == "j": return True
        if a == "v" and b == "j": return True
        return False
    if len(c) == 3:
        return c[0] == "s" and c[1] in "ptk" and c[2] in "rlwj"
    return False

def ipa(phones):
    """ARPAbet -> IPA with stress marks placed before the stressed syllable's onset.

    CMUdict marks compounds such as `outside` (AW1 ... AY1) and `engineering` with *two* primary
    stresses. Rendering both as the primary mark produced /ˈaʊˈtsaɪd/, which is not how a stress mark
    is read. Within one word the last primary wins and any earlier one is demoted to secondary, giving
    /ˌaʊtˈsaɪd/ — the conventional transcription.
    """
    prim = [i for i, p in enumerate(phones) if p.endswith("1")]
    if len(prim) > 1:
        phones = [p[:-1] + "2" if i in prim[:-1] else p for i, p in enumerate(phones)]
    out, nsyl = [], sum(1 for p in phones if p[:2] in VOWELS or p[:-1] in VOWELS)
    for i, ph in enumerate(phones):
        base, stress = (ph[:-1], ph[-1]) if ph[-1].isdigit() else (ph, None)
        sym = ARPA.get(base)
        if sym is None: return None
        if base == "AH" and stress == "0": sym = "ə"
        if base == "ER" and stress == "0": sym = "ɚ"
        if stress in ("1", "2") and nsyl > 1:
            mark = "ˈ" if stress == "1" else "ˌ"
            # Walk back only as far as the consonants that can legally begin an English syllable.
            # Taking every consonant back to the previous vowel split `outside` as ou-tside and printed
            # /ˌaʊˈtsaɪd/; /ts/ is not an English onset, so the t belongs to the first syllable's coda.
            j = len(out)
            while j > 0 and out[j-1][1] not in VOWELS and legal_onset([x for x, _ in out[j-1:]]):
                j -= 1
            out.insert(j, (mark, None))
        out.append((sym, base))
    return "".join(s for s, _ in out)

def lookup(word):
    e = CMU.get(word.lower())
    return ipa(e[0]) if e else None

STOP = set("""about above after again against because before being below between both cannot could
doesn during each every from have having here into itself just more most other over same should
some such than that their them then there these they this those through under until very were
what when where which while with would your yours""".split())

STRIP = re.compile(r"^(to|a|an|the|my|your|his|her|its|our|their|one's|someone's)\s+", re.I)
def headword(cell):
    w = re.sub(r"\*\*|`", "", cell).strip()
    w = re.sub(r"\([^)]*\)", "", w).strip()          # drop parentheticals
    w = w.split(" / ")[0].split(" vs ")[0].strip()   # take the first of an alternation
    w = STRIP.sub("", w).strip(" .,;:!?—-")
    return w

def gloss(cell):
    g = re.sub(r"\*\*|`", "", cell).strip()
    g = g.split(" — ")[0].split(" · ")[0].strip()
    return (g[:58] + "…") if len(g) > 60 else g

def expressions(text):
    rows, insec = [], False
    for l in text.split("\n"):
        if l.startswith("## "):
            insec = l[3:].strip().lower() == "expressions"; continue
        if not insec or not l.strip().startswith("|"): continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 2: continue
        if set("".join(cells)) <= set("-: "): continue
        if cells[0].lower() in ("expression", "word"): continue
        rows.append(cells)
    return rows

made, skipped = 0, []
for p in sorted(ROOT.glob("english-*.md"), key=lambda q: int(re.search(r"(\d+)", q.name).group(1))):
    text = p.read_text()
    if "\n## Words" in text: continue
    words, seen = [], set()
    for cells in expressions(text):
        hw = headword(cells[0])
        if not hw or hw.lower() in seen: continue
        parts = hw.split()
        if not 1 <= len(parts) <= 3: continue
        got = [lookup(w) for w in parts]
        if any(g is None for g in got): continue
        toks = [t.lower() for t in parts]
        if words and all(any(t in w.lower().split() for w, _, _ in words) for t in toks): continue
        seen.add(hw.lower())
        words.append((hw, " ".join(got), gloss(cells[1])))
        if len(words) == 8: break
    if len(words) < 2:
        # Phrase-based items ("have the nerve to + 동사", "Just because A doesn't mean B") yield no
        # headword short enough to look up. For those the useful row is not the phrase but the hard
        # word inside it, so fall back to picking multi-syllable content words out of the cells.
        for cells in expressions(text):
            for tok in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", re.sub(r"\*\*|`", "", cells[0])):
                lw = tok.lower()
                if lw in seen or lw in STOP: continue
                if any(lw in w.lower().split() for w, _, _ in words): continue
                e = CMU.get(lw)
                if not e: continue
                nsyl = sum(1 for ph in e[0] if ph[:-1] in VOWELS or ph[:2] in VOWELS)
                if nsyl < 2 and len(lw) < 6: continue
                i = ipa(e[0])
                if not i: continue
                seen.add(lw)
                words.append((tok, i, gloss(cells[1])))
                if len(words) == 6: break
            if len(words) == 6: break
    if len(words) < 2:
        skipped.append(p.name); continue
    block = "\n## Words\n" + "".join(f"| {w} | /{i}/ | {g} |\n" for w, i, g in words)
    idx = text.index("\n## Expressions")
    p.write_text(text[:idx] + block + text[idx:])
    made += 1

print(f"wrote ## Words into {made} file(s)")
if skipped: print(f"left alone ({len(skipped)}): {', '.join(skipped[:15])}{' …' if len(skipped)>15 else ''}")
