# AI slop audit: brochure site v3

Grade: **B-** for slop. That's lower than the A in `audit-v3.md`, which graded function (booking, speed, accessibility). On "does this look and read like generated work", v3 still leans on patterns that AI-built sites share right now.

The content is specific and true. The booking text writer, the payment table, the dated timeline and the sourced reviews are the parts no template would have. The slop is in the visual system and in a set of stock page components.

Photo captions were removed in this pass; see the house rule in the README.

## Design: 5/10

| Severity | Pattern | Where | Why it reads as generated |
|---|---|---|---|
| High | Off-white paper, serif display, 1px ink hairlines on everything | Whole site (`#fbfaf6`, Newsreader, rules under every heading, list and table) | "Broadsheet hairline rules" and "serif display on warm paper" are two of the most common AI looks right now. The teal accent and the logo card don't move it out of that cluster. |
| High | Numbered markers that encode nothing | Services (1 to 8), home "At the studio" (1 to 6) | Services aren't a sequence. The numbers are decoration in the "01 / 02 / 03" style. The whitening steps are a real sequence and keep theirs. |
| High | The same call to action four or five times a page | Topline phone, header "Book a visit", hero card buttons, the "Book by text" band above every footer, plus in-page buttons | The pre-footer CTA band repeated on every page is a conversion-template habit. A small practice's site doesn't need to ask on every scroll. |
| High | Floating card over the hero photo, with a soft drop shadow | Home | A trendy hero trope. The `0 22px 40px` blurred shadow is the generic "lifted card". |
| Medium | Two-up teaser cards: image, heading, blurb, "more" link | Home (Woodlands, whitening) | Stock blog-teaser block. |
| Medium | One testimonial set huge in serif | Home, Care outside the studio | Stock "big quote" band. |
| Medium | Alternating tinted section backgrounds | Every page (paper, tint, paper, tint) | Rhythm on autopilot, so every page has the same pulse. |
| Medium | Section title on the left, "All services" link on the right | Home | Template header row. |
| Medium | Spaced uppercase micro-labels | Card fields, footer headings | Justified once by the logo's "DENTAL HYGIENE CARE", then reused until it's a house style. |
| Low | Dot-and-line timeline with the last dot in the accent | About | Stock component. |
| Low | Italic serif "written-in" values on the cards | Home, book, contact | A conceit layered on a conceit. |

## Copy: 37/50 (stop-slop)

| Dimension | Score | Notes |
|---|---|---|
| Directness | 8 | Mostly plain statements of fact |
| Rhythm | 6 | Many paragraphs open "Rytel ..." and run the same length |
| Trust | 8 | Few rhetorical moves left |
| Authenticity | 7 | Specific to Bridgton, but none of it is in her voice |
| Density | 8 | Little filler |

Specific offenders:

- **Name stuffing.** "Rytel" opens most sentences on most pages. Real practice sites say "I" or "we", or vary it.
- **Throat-clearing:** "Here's how booking and payment work." (New patients)
- **Reflex lists of three:** "Cleanings, x-rays and checkups for adults and kids"; "cleans your teeth, takes x-rays and checks for gum disease and oral cancer".
- **Editorialising the research doesn't support:** "which matters for people who find a trip to an office hard or upsetting" (Care outside the studio).
- **Slogan teaser heading:** "Whitening in one visit".
- **Cute heading:** "Around town".
- **The design story:** "every patient leaves a dental visit holding one" (README) is a rationale written after the fact. It isn't on the site, but it drove the hero card, the booking card and the contact card.

## Not slop: keep

- The booking text writer: it fits how she actually books.
- The insurance and payment table.
- The dated timeline content and the sourced, dated reviews.
- The 55 Main Street sign photo as the opening image.
- Self-hosted fonts, a map that loads only on request, no captions.

## Fixes

Mechanical, no taste call needed:

1. Drop the numbers from the service lists.
2. Keep the header "Book a visit" button and one booking prompt per page, placed where it fits the content. Remove the "Book by text" band from every page.
3. Remove the drop shadow, and stop alternating section tints.
4. Rewrite the copy items above. Vary the subject, and use "I" or "we" where Rytel's own posts do.
5. Replace the teaser cards and the big-quote band with content in the flow of the page.

Needs a direction from Green Falls:

6. Move the visual system off "serif on warm paper with hairlines". Two directions grounded in the practice:
   - **Main Street sign:** the solid teal and white of the 55 Main Street sign, a sturdy sign-painter sans for headings, colour blocks instead of rules.
   - **Her own posts:** the clean white, black script logo and soft photography she already uses on Facebook and Instagram, so the site matches what patients already see from her.
