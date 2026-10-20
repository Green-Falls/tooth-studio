# Audit: brochure site v6

## Photos from social media

- **Facebook.** The public photos tab shows the same images collected on 2026-10-19 (59 in total). None shows Rytel.
- **Instagram.** Refuses logged-out visitors from this environment.
- **The only post-move interior.** A small inset in the March 2026 giveaway graphic shows the current treatment room: grey floor, desk monitor, a different chair. It is rotated, dim and covered by the graphic, so it can't be used. It does confirm the 82 Main Street room looks nothing like today's, so those photos must stay labelled as the first studio.
- **Conclusion.** New photos have to come from Rytel's phone or a shoot (see `photo-plan.md`).

## Design changes

References: Refero's live search needs a sign-in, so 21st.dev was used, with each reference adapted rather than copied:

| Reference | Used for |
|---|---|
| Centered Nav Header | Centred masthead: phone left, logo centre, request button right, links beneath |
| Editorial Image Hero | Centred logo-frame headline with the entrance as a wide band below |
| Feature Overview Bento | "Your hygienist": a deep teal quote tile beside two real figures (10+ years, 5.0 from 12 reviews) and a "one hygienist" tile |
| Bento Feature Grid | Service tiles: tinted fields with an icon each, on Home and Services |
| Simple Centered Footer | Centred footer with icons on the contact lines |

Also new: a deep teal "Booking takes one text" band with three numbered steps (text, get times back, come to 55 Main Street). The numbers mark a real sequence.

Kept from the anti-slop rules:
- Only the masthead, hero and footer are centred.
- Figures are real and sourced, not decorative.
- Icons each mean one thing.
- No photo captions.

## Checks (all passing)

- axe-core: 0 violations on every page at 1440px and 320px.
- No horizontal scroll at 1440, 768, 390 or 320px.
- No console errors, failed requests or third-party requests.
- Contact form: all paths tested.
