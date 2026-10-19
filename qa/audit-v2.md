# Audit: brochure site v2

Grade: **B-**. The slop is gone and the facts hold up, but v2 is a tidy document rather than a site someone would remember or that does the practice's real work.

## What held it back

| Problem | Detail |
|---|---|
| One layout, used everywhere | Every section is "heading in a left column, content on the right". 24 sections, one shape. A new metronome replaced the old one. |
| No visual idea | Thin rules and a teal accent read as careful, not as Tooth Studio. Nothing on the home page is memorable. |
| Weak opening image | The home page leads with a flat phone photo of vinyl siding. Her best photos (the red door, the Main Street sign in fall colour) are buried or missing. |
| Booking is a bare phone link | She books by text and phone, so the site's main job is getting a good first text. It only offered `sms:` with an empty message. |
| Third-party tracking on a health site | Google Fonts on every page and a Google Maps iframe that loads on arrival. Both send visitors' IPs to Google before they ask for anything. |
| Heavy images | Single 1400px JPEGs (150 to 450 KB) sent to phones. No `srcset`, no WebP. |
| Missing site basics | No 404 page, sitemap, robots.txt, apple-touch icon or FAQ structured data. No print styles for the contact page. |
| Copy still thin in places | "What she does" sat beside four links. The services page explained procedures without saying how long a visit takes or what happens first (we don't know yet, so v3 has to say so rather than guess). |

## What A+ means here

1. A booking flow built for how she works: fill in a short form, and it writes the text message for you and opens Messages. No server, nothing stored.
2. A visual idea from the practice itself: the appointment card. Her logo is already a ruled card, and every patient leaves a dental visit with one.
3. Varied page layouts, each matched to what the page is for.
4. The best real photos, with consistent colour correction and responsive sizes.
5. No third-party requests until a visitor asks for one (self-hosted fonts, click-to-load map).
6. Accessibility checked with axe, no overflow at 320px, and keyboard paths through the booking form.
7. Site basics: 404, sitemap, robots, icons, FAQ schema, print styles.

What still caps the grade, and needs Rytel: photos of the current treatment room, real hours, the membership price and the original logo file.
