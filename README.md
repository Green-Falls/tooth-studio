# Tooth Studio & Wellness website

A static brochure site for Tooth Studio & Wellness, the independent dental hygiene practice (IPDH) of Rytel Rowe at 55 Main Street, Bridgton, Maine.

| Page | File |
|---|---|
| Home | `index.html` |
| Services (including visits outside the studio) | `services.html` |
| Whitening | `whitening.html` |
| New patients (booking, hours, insurance, questions) | `new-patients.html` |
| About (story, dates, first studio, reviews) | `about.html` |
| Contact (visit request form, directions, map) | `contact.html` |
| Not found | `404.html` |

## Deploy

Upload the `site/` folder to any static host (Netlify, Cloudflare Pages, GitHub Pages). Point the host's 404 page at `404.html`.

**Connect the contact form before launch.** A static site can't send email by itself. Create a free form at formspree.io with Rytel's email (toothstudiomaine@gmail.com) as the recipient, paste its URL into `FORM_ENDPOINT` in `build.py`, and rebuild. Any service that accepts a JSON POST and answers `{"ok": true}` works. Until then, the form tells visitors it isn't connected and gives the phone number. Once the domain is live, set `SITE_URL` in `build.py` and rebuild: that adds canonical links, absolute share images and `sitemap.xml`.

## Editing

- Page content lives in `pages/*.html`. Each file starts with a one-line JSON comment: title, description, nav key, and optional `book`, `scripts` and `noindex`.
- The header, footer and "Book by text" strip are in `build.py`.
- Photos: add the original to `data/research/facebook/images/` (or anywhere), list it in `images.py` with an optional crop, and run `python3 images.py`. In a page, write `<img src="img/NAME.jpg" sizes="...">` and the build adds the `srcset`.
- Rebuild with `python3 build.py`. Commit `pages/`, `site/` and the scripts.
- `site/form.js` validates and sends the visit request form. `site/map.js` loads the Google map on request.

## Design

Her own look, as on her Facebook and Instagram: white, black ink and the script logo. The one accent is the teal of the 55 Main Street sign, used for actions. Jost for headings, because its geometric capitals match "DENTAL HYGIENE CARE" in the logo. Source Sans 3 for reading, with a plain zero so the phone number reads cleanly. Space separates sections; rules appear only in tables and lists of facts. The home hero is the 55 Main Street entrance, the door patients walk through.

The visit request form follows 21st.dev's "Appointment Booking Split" layout (reassurance and contact details beside the form), with sending, sent and error states from its "Contact Form" and category chips from "Support Ticket Form". It is the only card on the site.

## House rules

- **No captions on photos.** `build.py` refuses to build a page with one. Any context a photo needs goes in the page's own text or headings. Attributions on review quotes are not photo captions and stay.
- Because of that, photos of the first studio at 82 Main Street appear only on the About page, under the "Opening weekend, November 2024" heading, so they can't be taken for the current office.

## Sources and QA

- Every fact comes from `data/research/facebook/NOTES.md` and `MANIFEST.csv`.
- `qa/ai-slop-audit-v1.md`, `qa/audit-v2.md` and `qa/audit-v3.md` record each version's grade and what changed.

## To confirm with Rytel before launch

1. **A real hero photo.** The entrance is the best photo available. A portrait of Rytel in the treatment room at 55 Main Street would be stronger; Ashleigh London Photography, who shot the November 2024 open house, is a natural choice.
2. **Photos of the current studio.** All interior photos are from 82 Main Street, so they only appear on the About page. Shoot the treatment room and waiting area at 55 Main Street; the Services page has no photo until then.
3. **Hours.** None are published. The site says there are no fixed hours, and mentions Sunday visits only because reviewers do.
4. **Membership plan and whitening price.** What the plan includes and costs; whether to show a whitening price.
5. **Service and whitening wording.** The cleaning, fluoride and sealant descriptions and the four whitening steps describe standard practice. Check them against how she works. Her whitening graphics include her own "up to 14 shades brighter" claim.
6. **"Runs the studio herself."** The site says she does the cleanings herself. Confirm there's no second hygienist.
7. **Contact form.** Connect `FORM_ENDPOINT` (see Deploy) and confirm where requests should go and how fast she can reply.
8. **Name.** The site uses "Rytel Rowe, IPDH", as she posts. NPI lists "Rytel P Reynolds".
9. **Logo.** `img/logo.png` was traced from a 500px Facebook image. Swap in the original file.
