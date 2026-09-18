"""Section numbering for Knowledge Notes (jay, 2026-09-18: "make the Items from 1, Theory from 700, English
1000, Life 1300, Health 1400"; same day: "Investment should start from 800, and Foundation start 500", section named Invest, Theory renamed Theory). Each section numbers its items from its own base, so a number alone tells the
section. `k` is the 1-based position inside the section; `display` is what the reader sees.

Goals (jay, same day): 1,000 items done is the first turning point and gets a congratulation effect; 2,000 is the
final goal. _progress.js reads GOALS from here (kept in sync by hand; see docs/topics/README.md).
"""
BASE = {"nav-sec-blockchain": 1, "nav-sec-fundamentals": 500, "nav-sec-invest": 800, "nav-sec-english": 1000, "nav-sec-mindset": 1300, "health": 1400}
GOALS = (1000, 2000)

def display(navid, k): return BASE[navid] + k - 1
def position(navid, shown): return shown - BASE[navid] + 1
