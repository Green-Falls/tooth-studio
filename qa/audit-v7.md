# Audit: brochure site v7

Review of v6 found five weak spots. All fixed:

| v6 weak spot | v7 |
|---|---|
| Inner pages opened flat: title, small paragraph, white space | Every inner page opens on a tinted band with a deep teal panel of real facts. About and Whitening gained panels. |
| Whitening led with her Facebook flyers ("Glowing is a vibe", "VIBE") | `images.py` crops the clean photos out of both flyers: a before and an after, the GLO mouthpiece, and the GLO kit with shade guide and instruments. The page has a before/after pair, numbered steps beside the GLO photo, and the kit beside "Crowns and fillings" and "Cost". No text labels on the photos, per the no-captions rule. |
| Contact's empty grey map box | A deep teal location panel: pin icon, address, "Get directions" and "Show the map". |
| No way to text or call once a phone visitor scrolls | A fixed bottom bar on phones: Text, Call, Request. It respects the iPhone home-bar inset, and the page pads its bottom so the bar never covers the footer. |
| Nothing on the site moved | On the home page the logo frame draws itself in on load: top, right, bottom, left, then the buttons and the bottom label rise in. With reduced motion turned on, the frame is complete from the start. |

Also: the service tiles use a compact icon-left layout on phones, so the six services take about half the scrolling.

## Checks (all passing)

- axe-core: 0 violations on every page at 1440px and 320px.
- No horizontal scroll at 1440, 768, 390 or 320px.
- No console errors, failed requests or third-party requests.
- Contact form: all paths tested.
- Animation checked mid-draw, and with reduced motion on.
