#!/usr/bin/env python3
"""Korean public holidays and business-day arithmetic (jay, 2026-09-25: "define category New as the
new items during two business day based on Korea holiday system").

A business day here is a weekday (Mon–Fri) that is not a Korean public holiday. Weekends and the
dates in HOLIDAYS are skipped.

Why a hardcoded table: every script in this repo is zero-dependency and runs offline during a static
build, so a pip package or an API key is the wrong shape. The cost is that the table has to be
extended by hand, so `business_days_since` REFUSES to guess: if it is asked about a date in a year
the table does not cover, it raises. A wrong answer about a holiday is worse than a loud failure.

Lunar-calendar holidays (설날, 부처님오신날, 추석) move every year, and 대체공휴일 (substitute
holidays) depend on which day of the week a holiday lands on, so each year has to be added
deliberately. To extend: add the year to HOLIDAYS and to COVERED, with a source.
"""
import datetime

# 2026, checked 2026-09-25 against Korean holiday calendars (16 weekday holidays, 4 substitutes:
# 3/2, 5/25, 8/17, 10/5). Dates that fall on a weekend are listed too — harmless, since weekends are
# already skipped, and it keeps the table readable as the official list.
HOLIDAYS = {
    datetime.date(2026, 1, 1):   "신정",
    datetime.date(2026, 2, 16):  "설날 연휴",
    datetime.date(2026, 2, 17):  "설날",
    datetime.date(2026, 2, 18):  "설날 연휴",
    datetime.date(2026, 3, 1):   "삼일절 (일요일)",
    datetime.date(2026, 3, 2):   "삼일절 대체공휴일",
    datetime.date(2026, 5, 5):   "어린이날",
    datetime.date(2026, 5, 24):  "부처님오신날 (일요일)",
    datetime.date(2026, 5, 25):  "부처님오신날 대체공휴일",
    datetime.date(2026, 6, 6):   "현충일 (토요일; 대체공휴일 대상 아님)",
    datetime.date(2026, 8, 15):  "광복절 (토요일)",
    datetime.date(2026, 8, 17):  "광복절 대체공휴일",
    datetime.date(2026, 9, 24):  "추석 연휴",
    datetime.date(2026, 9, 25):  "추석",
    datetime.date(2026, 9, 26):  "추석 연휴 (토요일)",
    datetime.date(2026, 10, 3):  "개천절 (토요일)",
    datetime.date(2026, 10, 5):  "개천절 대체공휴일",
    datetime.date(2026, 10, 9):  "한글날",
    datetime.date(2026, 12, 25): "성탄절",
}
# UNRESOLVED for 2026: whether 추석 falling partly on Saturday 9/26 produces a substitute on Monday
# 9/28. The calendars consulted list exactly four substitutes and do not include it, so it is not in
# the table. If it turns out to be a holiday, add it — the only effect is that one item would stay
# NEW a day longer than it should have.

COVERED = {2026}   # years the table is complete for. Extend deliberately, with a source.


def is_holiday(d: datetime.date) -> bool:
    return d in HOLIDAYS


def is_business_day(d: datetime.date) -> bool:
    """Mon–Fri and not a Korean public holiday."""
    return d.weekday() < 5 and d not in HOLIDAYS


def business_days_since(added: datetime.date, today: datetime.date) -> int:
    """Business days strictly after `added`, up to and including `today`.

    added=Mon, today=Tue -> 1.  added=Fri, today=Mon -> 1 (weekend skipped).
    Returns 0 if today is on or before added.
    """
    for year in {added.year, today.year}:
        if year not in COVERED:
            raise ValueError(
                f"kr_holidays: no holiday table for {year}. Add it to HOLIDAYS and COVERED in "
                f"scripts/kr_holidays.py before relying on business-day arithmetic."
            )
    if today <= added:
        return 0
    n, d = 0, added + datetime.timedelta(days=1)
    while d <= today:
        if is_business_day(d):
            n += 1
        d += datetime.timedelta(days=1)
    return n
