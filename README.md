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

**Connect the contact form before launch.** A static site can't send email by itself. Create a free form at formspree.io with Rytel's email (toothstudiomaine@gmail.com) as the recipient, paste its URL into `FORM_ENDPOINT` in `build.py`, and rebuild. Any service that accepts a JSON POST and answers `{"ok": true}` works. Until then, the form tells visitors it isn't connected and gives the phone number. Once the domain is live, set `SITE_URL` in `build.py` and rebuild: that adds canonical links, absolute share images, `sitemap.xml` and the site URL in the structured data. See `qa/seo-aeo.md` for search and AI-answer optimisation, and the off-site steps (Google Business Profile, listings) that matter most for local search.

## Client preview

`.github/workflows/preview.yml` publishes the site to **https://toothstudio.greenfalls.co** on every push to `main`. It builds with `PREVIEW_HOST` set, so every page is marked noindex and `robots.txt` blocks crawlers. The preview stays out of search and won't compete with her real domain later.

One-time setup:
1. GitHub: Settings → Pages → Build and deployment → Source: **GitHub Actions**.
2. Namecheap (greenfalls.co DNS): add a **CNAME** record, host `toothstudio`, value `green-falls.github.io`.
3. GitHub: Settings → Pages → Custom domain: `toothstudio.greenfalls.co`, save, then tick **Enforce HTTPS** once the certificate is issued (can take up to an hour).
4. Run the workflow (Actions → preview → Run workflow), or push to `main`.

The contact form says it isn't connected until `FORM_ENDPOINT` is set.

## Editing

- Page content lives in `pages/*.html`. Each file starts with a one-line JSON comment: title, description, nav key, and optional `scripts` and `noindex`.
- The utility bar, header, footer and phone action bar are in `build.py`. Icons are written as `<span class="icon" data-icon="NAME"></span>` and inlined from `icons/`.
- Photos: add the original to `data/research/facebook/images/` (or anywhere), list it in `images.py` with an optional crop, and run `python3 images.py`. In a page, write `<img src="img/NAME.jpg" sizes="...">` and the build adds the `srcset`.
- Rebuild with `python3 build.py`. Commit `pages/`, `site/` and the scripts.
- `site/form.js` validates and sends the visit request form. `site/map.js` loads the Google map on request.

## Design

Her own look, built from her logo. The logo is a script wordmark inside a thin ink frame that the script breaks at the top, with "DENTAL HYGIENE CARE" in spaced capitals on the bottom line. The home hero repeats that construction: the headline breaks the top of a thin frame and "55 MAIN STREET · BRIDGTON, MAINE" sits on the bottom line. No second script font: hers stays the only one.

White and black ink, with the teal of the 55 Main Street sign for actions. Jost for headings (its geometric capitals match the logo's), Source Sans 3 for reading (plain zero, so the phone number reads cleanly). Rules only in tables and fact lists. The hero photo is the 55 Main Street entrance. Whitening uses clean photos cropped out of her own flyers.

**Filling in for missing photos.** Until there are photos of the current office and of Rytel, colour and icons carry those spots:
- A deep teal panel (the sign's teal, darkened) holds Rytel's quote on the home page and the key facts at the top of every inner page. Each panel carries the faint tooth outline that sits behind her wordmark.
- Phosphor "light" icons (MIT, in `icons/`, inlined by the build) mark each service and the contact details. Their thin line matches the logo. Each icon means one thing: tooth for cleanings, magnifying glass for screening, scan for x-rays, shield for fluoride, brush for sealants, sparkle for whitening, baby for children, first-aid kit for dentist referrals, house for on-site visits, wheelchair for access.

When real photos arrive, they should replace the panels first.

**Layout.**
- **Header.** A deep teal utility bar carries the contact actions: the address and "Taking new patients" on the left, "Call or text (207) 599-6459" and "Request a visit" on the right. Below it, the masthead is just the logo, centred like the logo itself, with the page links in a centred row.
- **Phones.** The utility bar hides on phones, where a fixed Text / Call / Request bar sits at the bottom of the screen.
- **Home hero.** The logo frame is centred, and draws itself in on load unless reduced motion is on. The entrance photo runs as a wide band below it.
- **Inner pages.** Each opens on a tinted band with a deep teal fact panel.
- **Footer.** Centred. Everything else is left-aligned.
- **References from 21st.dev:** "Centered Nav Header" (adapted), "Editorial Image Hero", "Feature Overview Bento" (the "Your hygienist" grid), "Bento Feature Grid" (service tiles) and "Simple Centered Footer".
- **Numbers are real:** 10+ years, 5.0 from 12 Google reviews, 2,000 supervised hours for the IPDH licence. Numbered steps appear only where they are a real sequence (booking, whitening).

**Reviews.**
- Quoted as written, with curly quotes hung into the margin and the key phrase marked in teal.
- Shortened reviews show "…".
- The About page pairs them with a rating summary that links to the real reviews on Google and Facebook.

The visit request form follows 21st.dev's "Appointment Booking Split" layout, with states from its "Contact Form" and chips from "Support Ticket Form". It is the only card on the site.

`qa/competitors.md` compares the site with Bridgton Dental Associates, Main Street Dental and Mountain View Dentistry, and lists what to avoid so Tooth Studio doesn't look like them.

## House rules

- **No captions on photos.** `build.py` refuses to build a page with one. Any context a photo needs goes in the page's own text or headings. Attributions on review quotes are not photo captions and stay.
- Because of that, photos of the first studio at 82 Main Street appear only on the About page, under the "Opening weekend, November 2024" heading, so they can't be taken for the current office.

## Sources and QA

- Every fact comes from `data/research/facebook/NOTES.md` and `MANIFEST.csv`.
- `qa/` holds an audit for each version (`ai-slop-audit-v1.md`, `audit-v2.md` to `audit-v8.md`, `ai-slop-audit-v3.md`), plus `competitors.md`.
- `photo-plan.md` lists where better photos can come from, with a shot list mapped to the site.
- Structured data, the FAQ schema and `llms.txt` are generated by `build.py` from the same facts as the pages.

## To confirm with Rytel before launch

1. **A real hero photo.** The entrance is the best photo available. A portrait of Rytel in the treatment room at 55 Main Street would be stronger; Ashleigh London Photography, who shot the November 2024 open house, is a natural choice.
2. **Photos of the current studio.** All interior photos are from 82 Main Street, so they only appear on the About page. Shoot the treatment room and waiting area at 55 Main Street; the Services page has no photo until then.
3. **Hours.** None are published. The site says there are no fixed hours, and mentions Sunday visits only because reviewers do.
4. **Membership plan and whitening price.** What the plan includes and costs; whether to show a whitening price.
5. **Service and whitening wording.** The cleaning, fluoride and sealant descriptions and the four whitening steps describe standard practice. Check them against how she works. Her whitening graphics include her own "up to 14 shades brighter" claim.
6. **"Runs the studio herself."** The site says she does the cleanings herself. Confirm there's no second hygienist.
7. **Contact form.** Connect `FORM_ENDPOINT` (see Deploy) and confirm where requests should go and how fast she can reply.
8. **Name.** The site uses "Rytel Rowe, IPDH", as she posts. NPI lists "Rytel P Reynolds".
9. **Logo.** `img/logo.png` was traced from a 500px Facebook image. The site now leans on the logo, so the original vector file (SVG, PDF or AI) matters more than anything else on this list except photos.
