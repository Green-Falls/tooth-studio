# SEO and AEO (answer engines)

## Done on the site

| Area | State |
|---|---|
| Titles | Unique on every page, 40 to 61 characters, place name included |
| Meta descriptions | Unique, 136 to 154 characters, key terms first |
| Headings | One H1 per page, each naming what and where (e.g. "Dental hygiene services in Bridgton", "Professional teeth whitening in Bridgton") |
| Structured data | On every page: the studio as a `MedicalClinic` with name, address, phone, email, area served, map link, services, insurance, `isAcceptingNewPatients`, NPI 1770323479, and Facebook/Instagram as `sameAs`. Rytel as a `Person` with her IPDH credential. Page types: `AboutPage`, `ContactPage`, whitening `Service`, and an `FAQPage` generated from the visible FAQ so the two can't drift. No self-published star ratings, which Google ignores for local businesses. |
| Answer-first FAQ | New patients page: 10 questions people ask search engines and AI assistants ("Is Tooth Studio taking new patients?", "What is an IPDH?", "Does it accept MaineCare?", "Where is it?"). Each answer leads with a direct sentence. |
| `llms.txt` | Plain-text summary of the practice at the site root, built from the same facts |
| Social previews | 1200×630 JPEG share image, Open Graph and Twitter card tags |
| Images | Alt text on every image; WebP with responsive sizes |
| Speed and access | Self-hosted fonts, no third-party requests on load, 0 axe violations, works down to 320px |
| Crawling | `robots.txt` allows all. `sitemap.xml` and canonical links are generated once `SITE_URL` is set (tested with a stand-in domain). |

## Needs a domain

Set `SITE_URL` in `build.py` and rebuild. That adds:
- canonical links
- absolute share-image URLs
- `sitemap.xml`
- the sitemap line in `robots.txt`
- the `url` in the structured data

Then submit the sitemap in Google Search Console and Bing Webmaster Tools.

## Off-site: the biggest local factors, all outside the code

1. **Google Business Profile.** It lists no website and no hours. Add the site URL and her booking hours (or "by appointment"). Add the photos from `photo-plan.md` as they arrive. Choose the most accurate primary category; it is a hygiene practice, not a dentist.
2. **Facebook page.** It lists no website. Add it. Instagram's bio link should point to the site too.
3. **Consistent name, address and phone everywhere.** Use one form: "Tooth Studio & Wellness, 55 Main Street, 1st floor, Bridgton, ME 04009, (207) 599-6459". Known mismatches:
   - The From the First Tooth referral list still shows 82 Main Street, Unit 1. Ask them to update it.
   - The NPI registry shows 576 Main Street. Update it through NPPES.
   - An April 2025 flyer used the old Instagram handle @toothstudiomaine.
   - Rytel's name appears as Rowe (her posts) and Reynolds (NPI). Pick one public name.
4. **Listings to claim with the same details:** Apple Business Connect (Apple Maps and Siri), Bing Places, Yelp, Healthgrades. Also the Maine Dental Hygienists' Association IPDH list.
5. **Reviews.** Keep asking happy patients for Google reviews. They feed the map pack and AI answers. Reply to each one.
6. **Local links.** Woodlands Memory Care, Bridgton's Free Little Pantry, and the Lakes Region chamber are natural places to be listed or mentioned with a link.
