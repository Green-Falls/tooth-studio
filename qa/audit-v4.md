# Audit: brochure site v4

Slop grade: **B+**, up from B- for v3. What still holds it back is the photography. That needs a shoot, not code.

## Changes from v3

| v3 slop finding | v4 |
|---|---|
| Off-white paper, serif display, hairlines everywhere | Her own look: white, black ink, the script logo. Jost headings, Source Sans 3 text. Rules only in tables and fact lists. |
| Numbered service markers | Removed. Only the whitening steps, a real sequence, keep numbers. |
| Booking prompt four or five times a page | One header button ("Request a visit") and one prompt where a page needs it. The pre-footer band and the top phone strip are gone; the phone number sits in the header. |
| Floating card with a drop shadow over the hero | A plain split: headline and one action beside the photo. |
| Teaser cards and a giant quote band | Content in the flow: a short section with one photo; reviews at reading size. |
| Alternating section tints | One tinted band per page at most, where it groups something (insurance, the children and dentist pair). |
| Name stuffing, "Here's how", lists of three | Copy rewritten with varied subjects. Rytel's own words, from her October 2026 post, carry the "Your hygienist" section. |
| Roadside sign as the hero | The 55 Main Street entrance: the porch, the ramp and the sign listing the studio. |
| "Care outside the studio" in the nav | Folded into Services as "Visits outside the studio" and removed from the nav. |
| "Write my text" booking page | Replaced by a visit request form on the Contact page (see below). |
| Photo captions | None; `build.py` refuses to build a page with one. |

## The form

Modelled on 21st.dev components, adapted to vanilla HTML, CSS and JS:
- **"Appointment Booking Split"** for the layout: reassurance and contact details beside the form.
- **"Contact Form"** for the sending, sent and error states.
- **"Support Ticket Form"** for the category chips.

Refero's live search needs a sign-in that wasn't available in this session, so its bundled anti-slop guidance was used instead. The form is the only card on the site.

Behaviour tested end to end:
- Required name and phone, with inline errors that move focus to the first problem field.
- Phone numbers checked for a full 10 digits.
- Email becomes required when "Email" is the chosen reply method.
- A honeypot field catches spam bots.
- Sending state, then a confirmation that uses the first name and the reply method.
- A server error keeps everything the visitor typed and offers the phone number.
- With no endpoint configured, the form says it isn't connected rather than pretending to send.

## Bugs found and fixed in QA

- Atkinson Hyperlegible (the first body font) draws a slashed zero, so the phone number read "(2Ø7) 599-6459". Replaced with Source Sans 3.
- `.form { display: grid }` overrode the `hidden` attribute, so the form stayed visible after sending. A global `[hidden] { display: none !important }` fixes it.
- On phones the form sat below the whole contact list. A grid-area order now puts it straight after the intro.

## Checks (all passing)

- axe-core (WCAG 2.0/2.1 A and AA, plus best practice): 0 violations on every page at 1440px and 320px.
- No horizontal scroll at 1440, 768, 390 or 320px.
- No console errors, failed requests or third-party requests.

## Still needed from Rytel

- A portrait of her at the chair in the 55 Main Street treatment room. That's the hero this site wants.
- Interior photos of 55 Main Street.
- Hours, the membership plan details and a whitening price.
- The original logo file.
- A Formspree (or similar) endpoint for the form.
