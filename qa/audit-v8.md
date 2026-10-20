# Audit: brochure site v8

## Utility nav

- **Desktop.** "Call or text" and "Request a visit" moved out of the masthead into a deep teal utility bar, with the address and "Taking new patients" on its left. The masthead is now only the centred logo and links.
- **Tablet.** The links fold into Menu.
- **Phones.** The bar hides; the fixed Text / Call / Request bar at the bottom does the same job.

## Review treatment

| Before | After |
|---|---|
| Straight typewriter quotes ("…") | Curly quotes (“…”), the opening mark hung into the margin |
| Long quotes, no way to scan for the point | The key phrase in each review marked in soft teal |
| Rating in one tile, reviews somewhere else, nothing checkable | About: a rating summary (5.0, 12 Google reviews, both Facebook reviewers recommend) with links to read them on Google and Facebook |
| Two home-page quotes, both from adults booking for themselves | Three, one per audience: adults, parents, families of someone in memory care |
| A home quote shortened by changing the reviewer's words | Restored word for word. Shortening only with "…" |

## Stale layout and design found and fixed

- **Seven dead style rules from earlier versions:** the old header, the "or call" line, the old whitening steps and pair grid, the old service lists, the small button.
- **A regression from removing them.** The cleanup also deleted the phone rule that stacks the tiles, bento and before/after photos into one column, which caused a 14px sideways scroll at 320px. Restored, with columns that can shrink (`minmax(0, 1fr)`), so long words wrap instead of pushing the page wider.
- **The "Whitening" stub at the bottom of Services** (a heading and one sentence) became a full-width link row under the service tiles.
- **The rating summary used `<aside>` inside a section,** which axe flags as a misplaced landmark. Now a plain `<div>`.
- **On phones, the two figure tiles (10+ years, 5.0)** sit side by side instead of taking a full row each.
- **README** described the old header, a "Book by text" strip that no longer exists, and only three audits. Updated.

## Checks (all passing)

- axe-core: 0 violations on every page at 1440px and 320px.
- No horizontal scroll at 1440, 768, 390 or 320px.
- No console errors, failed requests or third-party requests.
- Contact form: all paths tested.
