# Audit: brochure site v3

Grade for what can be built without the client: **A**. It becomes A+ once Rytel supplies the four items at the bottom; no amount of build work can replace those.

## What changed from v2 (B-)

| v2 problem | v3 |
|---|---|
| One layout everywhere | Each page has its own layout: hero with a card laid over the photo, a numbered service index, picture stories, a single large review, a payment table, steps across the page, disclosure FAQ, a vertical timeline, masonry reviews. |
| No visual idea | The appointment card. Her logo is already a ruled card, so the home hero, the booking page and the contact page are drawn as one: a double rule, spaced-caps field labels, and italic "written-in" values. |
| Weak opening image | The 55 Main Street roadside sign in autumn, cropped to show "Tooth Studio & Wellness" on the sign and to leave out a campaign yard sign in the original. |
| Booking was a bare `sms:` link | `book.html` asks six short questions and writes the text: who it's for, new or returning, the visit, insurance, days and times. It opens Messages with the text filled in, or copies it, or emails it. Nothing is stored or sent by the site. |
| Third-party requests on a health site | Fonts are self-hosted. The Google map loads only when a visitor presses "Show the map". QA found zero outside requests on every page. |
| Heavy images | `images.py` colour-corrects every photo the same way and writes WebP at 480 to 1600px with `srcset`. Pages weigh about 180 to 490 KB on a phone. |
| Missing basics | 404 page, robots.txt, sitemap (once the domain is set), apple-touch icon, FAQ structured data, print styles. |

## Checks run (all passing)

- axe-core (WCAG 2.0/2.1 A and AA, plus best practice) on every page at 1440px and 320px: 0 violations.
- No horizontal scroll at 1440, 768, 390 or 320px on any page.
- No console errors, no failed requests, no third-party requests.
- Every internal link and anchor resolves; every image and `srcset` file exists.
- Structured data parses as JSON on every page.
- Booking flow tested end to end, for example: "Hi Rytel, this is Sam. I'd like to book a cleaning and whitening for my child. We're new patients. We have MaineCare. Tuesdays or Saturdays work best, in the afternoon. Thank you!"
- No em dashes or slogan headings in site copy (dashes appear only inside verbatim reviews).

## Bug found and fixed during QA

The build matched photo variants by prefix, so `woodlands` also picked up `woodlands-sign` and served the wrong photo at some screen widths. It now matches exact names, and QA checks that each `srcset` holds one photo.

## What's left for A+ (needs Rytel)

1. Photos of the treatment room and waiting area at 55 Main Street. Every interior photo is from the first studio and is captioned that way.
2. Hours, or a clear "by appointment" policy in her words.
3. The membership plan: what it includes and what it costs. A whitening price, if she wants one shown.
4. The original logo file. The current one is traced from a 500px Facebook image.

She should also read the service descriptions and the whitening steps, which describe standard hygiene and GLO practice rather than anything she has written.
