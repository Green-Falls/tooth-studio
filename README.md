# Tooth Studio & Wellness website

A static brochure site for Tooth Studio & Wellness, the independent dental hygiene practice (IPDH) of Rytel Rowe at 55 Main Street, Bridgton, Maine.

| Page | File |
|---|---|
| Home | `index.html` |
| Book a visit (writes the booking text) | `book.html` |
| Services | `services.html` |
| Whitening | `whitening.html` |
| Care outside the studio | `care-outside-the-studio.html` |
| New patients (booking, hours, insurance, questions) | `new-patients.html` |
| About (story, timeline, first studio, reviews) | `about.html` |
| Contact (card, click-to-load map, photos) | `contact.html` |
| Not found | `404.html` |

## Deploy

Upload the `site/` folder to any static host (Netlify, Cloudflare Pages, GitHub Pages). Point the host's 404 page at `404.html`. Once the domain is live, set `SITE_URL` in `build.py` and rebuild: that adds canonical links, absolute share images and `sitemap.xml`.

## Editing

- Page content lives in `pages/*.html`. Each file starts with a one-line JSON comment: title, description, nav key, and optional `book`, `scripts` and `noindex`.
- The header, footer and "Book by text" strip are in `build.py`.
- Photos: add the original to `data/research/facebook/images/` (or anywhere), list it in `images.py` with an optional crop, and run `python3 images.py`. In a page, write `<img src="img/NAME.jpg" sizes="...">` and the build adds the `srcset`.
- Rebuild with `python3 build.py`. Commit `pages/`, `site/` and the scripts.
- `site/book.js` writes the booking message. `site/map.js` loads the Google map on request.

## Design

The idea is an appointment card. Her logo is a ruled card with spaced caps beneath the script, and every patient leaves a dental visit holding one. Cards on the home page, booking page and contact page use a double rule, spaced-caps field labels and italic "written-in" values. Ink on paper, with one accent: the teal of the 55 Main Street sign. Newsreader for headings, Public Sans for text, both self-hosted.

## House rules

- **No captions on photos.** `build.py` refuses to build a page with one. Any context a photo needs goes in the page's own text or headings. Attributions on review quotes are not photo captions and stay.
- Because of that, photos of the first studio at 82 Main Street appear only on the About page, under the "Opening weekend, November 2024" heading, so they can't be taken for the current office.

## Sources and QA

- Every fact comes from `data/research/facebook/NOTES.md` and `MANIFEST.csv`.
- `qa/ai-slop-audit-v1.md`, `qa/audit-v2.md` and `qa/audit-v3.md` record each version's grade and what changed.

## To confirm with Rytel before launch

1. **Photos of the current studio.** All interior photos are from 82 Main Street, so they only appear on the About page. Shoot the treatment room and waiting area at 55 Main Street; the Services page has no photo until then.
2. **Hours.** None are published. The site says there are no fixed hours, and mentions Sunday visits only because reviewers do.
3. **Membership plan and whitening price.** What the plan includes and costs; whether to show a whitening price.
4. **Service and whitening wording.** The cleaning, fluoride and sealant descriptions and the four whitening steps describe standard practice. Check them against how she works. Her whitening graphics include her own "up to 14 shades brighter" claim.
5. **"Runs the studio herself."** The site says she does the cleanings herself. Confirm there's no second hygienist.
6. **Booking text.** Confirm she's happy receiving texts in the format `book.html` writes.
7. **Name.** The site uses "Rytel Rowe, IPDH", as she posts. NPI lists "Rytel P Reynolds".
8. **Logo.** `img/logo.png` was traced from a 500px Facebook image. Swap in the original file.
