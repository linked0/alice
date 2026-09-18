# Key expressions — one file per detail page

`<page>.md` here is rendered onto `docs/topics/<page>.html` by `scripts/add-vocab.py` as the
"Key expressions / 핵심 표현" table at the end of both articles (jay, 2026-09-18). Two columns:

```
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| treasury desk | 자금 운용 데스크 · 은행·기업 안에서 현금과 국채를 굴리는 부서. "a score that a treasury desk reads" |
```

Rows cover words, phrases **and** acronyms / regulation / standard / institution names (BMR, MiFID II,
ETP NAV …); for an acronym put the full English form in parentheses after the Korean meaning.
Column 2 is the Korean meaning, then ` · `, a short Korean note on usage, then the fragment of the
page where it appears in quotes. No `|` inside a cell. Edit the file, then run
`python3 scripts/add-vocab.py <page>`. Rules in [../README.md](../README.md).
