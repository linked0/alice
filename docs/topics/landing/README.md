# Where it lands in Jayverse — backfill source, one file per detail page

`<page>.md` here holds two bullet lists, under `## en` and `## ko`, rendered by
`scripts/add-landing.py` as the "Where it lands in Jayverse / Jayverse에서의 위치" section on
`docs/topics/<page>.html` (jay, 2026-09-18: every detail page has this section). Pages written with
`add-tech-item.py` carry the section in their own markdown and have no file here. Each bullet: a bold
lead naming the service and the decision, then one or two sentences concrete enough to act on.
