# Tooth Studio & Wellness website

A static brochure site for Tooth Studio & Wellness, the independent dental hygiene practice (IPDH) of Rytel Rowe at 55 Main Street, Bridgton, Maine.

| Page | File |
|---|---|
| Home | `index.html` |
| Services | `services.html` |
| Whitening | `whitening.html` |
| Care outside the studio | `care-outside-the-studio.html` |
| New patients (booking, insurance, questions) | `new-patients.html` |
| About (timeline, first studio, reviews) | `about.html` |
| Contact (map, directions) | `contact.html` |

## Editing

- Edit page content in `pages/*.html`. Each file starts with a one-line JSON comment holding the page title, description and nav key.
- The shared header, footer and "Book by text or phone" strip live in `build.py`.
- Run `python3 build.py` to regenerate `site/`. Commit both `pages/` and `site/`.
- `site/` is the deployable folder (Netlify, Cloudflare Pages, GitHub Pages or any static host). No other build step.
- Sources: `data/research/facebook/NOTES.md` and `MANIFEST.csv`. Every fact on the site comes from there.
- `qa/ai-slop-audit-v1.md` explains why the first one-page version was replaced.

## Design

Ink on paper, taken from her logo: the thin ruled box around the wordmark, spaced caps, square corners. The one accent colour is the teal of the 55 Main Street sign. Newsreader for headings, Public Sans for text.

## To confirm with Rytel before launch

1. **Photos of the current studio.** The interior photos are from the first studio at 82 Main Street and are labelled that way on the About page. Shoot the treatment room at 55 Main Street.
2. **Hours.** None are published. The site says there are no fixed hours and mentions Sunday visits only because reviewers do.
3. **Whitening steps and price.** The "How it works" steps describe the standard GLO Science process. Check they match how she does it, and whether she wants a price shown.
4. **Membership plan.** What it includes and what it costs.
5. **Service descriptions.** Check the cleaning, fluoride and sealant wording against what she offers.
6. **Name.** The site uses "Rytel Rowe, IPDH", as she posts. NPI lists "Rytel P Reynolds".
7. **Logo.** `img/logo.png` was traced from a 500px Facebook image. Swap in the original file.
8. **Domain.** Add a canonical URL once she has one.
