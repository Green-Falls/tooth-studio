# Audit: brochure site v5

Prompted by three notes: too much whitespace; make sure we don't look like the local dentists; use colour and icons where photos are missing.

## Changes

- **Spacing.** Section spacing cut from up to 112px to up to 76px. Headings, header, page tops, grids and footer tightened. Home page height fell from 3,330px to about 3,085px even with new content. On About, the dates and reviews now use two columns instead of a narrow column beside empty space.
- **Distinct from local dentists** (see `competitors.md`):
  - The v4 hero copied the Bridgton Dental Associates formula. The hero is now built like her logo: a thin frame broken by the headline, with spaced capitals on the bottom line.
  - The headline leads with what a dental office can't say: "Teeth cleaning in Bridgton, booked by text."
  - The primary button texts her directly.
- **Logo as identity.** Its construction (frame, monoline, spaced caps) drives the hero, panels and icons. No second script font.
- **Colour and icons for missing photos.** Deep teal panels with the logo's tooth outline replace the absent portrait and fill the photo-less page tops. Phosphor light icons mark each service and the contact details.

## Checks (all passing)

- axe-core: 0 violations on every page at 1440px and 320px.
- No horizontal scroll at 1440, 768, 390 or 320px.
- No console errors, failed requests or third-party requests.
- Contact form: every validation, sending, sent, error and "not connected" path tested.

## Still needed

- Photos: Rytel at the chair and the 55 Main Street interior. These should replace the teal panels first.
- The original logo file (vector), now that the site leans on it.
- A form endpoint, hours, the membership plan and a whitening price.
