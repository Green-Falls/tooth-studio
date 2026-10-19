#!/usr/bin/env python3
"""Build the Tooth Studio site: wrap each pages/*.html body in the shared header and footer.

Each page file starts with one line of JSON in an HTML comment:
  <!-- {"title": "...", "description": "...", "nav": "services"} -->
Optional keys: "book": false hides the closing booking strip, "scripts": ["book.js"],
"noindex": true keeps a page out of search and the sitemap.

Photos: write <img src="img/NAME.jpg" sizes="..."> and the build adds a srcset of the
WebP files images.py made for NAME. Run images.py first if photos changed.

Output goes to site/. Run: python3 build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
PAGES = ROOT / "pages"
OUT = ROOT / "site"

# Set this once the domain is live; it turns on canonical links, absolute share
# images and the sitemap.
SITE_URL = ""

SITE = "Tooth Studio & Wellness"
PHONE = "(207) 599-6459"
TEL = "+12075996459"

NAV = [
    ("services", "services.html", "Services"),
    ("whitening", "whitening.html", "Whitening"),
    ("outside", "care-outside-the-studio.html", "Care outside the studio"),
    ("new", "new-patients.html", "New patients"),
    ("about", "about.html", "About"),
    ("contact", "contact.html", "Contact"),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}{canonical}<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta name="theme-color" content="#fbfaf6">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/newsreader.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/public-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="topline"><div class="wrap">
    <span>55 Main Street, 1st floor, Bridgton, Maine</span>
    <span>Call or text <a href="tel:{tel}">{phone}</a></span>
  </div></div>
  <div class="wrap header-inner">
    <a class="brand" href="index.html"><img src="img/logo.png" alt="{site}, dental hygiene care" width="556" height="158"></a>
    <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
    <a class="button primary small header-book" href="book.html"{book_current}>Book a visit</a>
    <details class="menu"><summary>Menu</summary><ul>{nav_menu}</ul></details>
  </div>
</header>
<main id="main">
"""

BOOK = """<section class="book-strip" aria-label="Book a visit">
  <div class="wrap">
    <div>
      <h2>Book by text</h2>
      <p>Answer a few questions and the site writes the text for you. Or call {phone}.</p>
    </div>
    <div class="buttons">
      <a class="button primary" href="book.html">Write my text</a>
      <a class="button" href="tel:{tel}">Call {phone}</a>
    </div>
  </div>
</section>
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="img/logo.png" alt="{site}" width="556" height="158" loading="lazy">
        <address>55 Main Street, 1st floor<br>Bridgton, ME 04009</address>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:{tel}">{phone}</a>, call or text</li>
          <li><a href="mailto:toothstudiomaine@gmail.com">toothstudiomaine@gmail.com</a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61562688787508">Facebook</a> · <a href="https://www.instagram.com/toothstudioandwellness/">Instagram</a></li>
        </ul>
      </div>
      <div>
        <h2>Pages</h2>
        <ul>{nav_footer}</ul>
      </div>
    </div>
    <p class="legal">Tooth Studio &amp; Wellness LLC. Rytel Rowe, Independent Practice Dental Hygienist. In network with all Delta Dental plans and MaineCare.</p>
  </div>
</footer>
{scripts}</body>
</html>
"""

IMG = re.compile(r'<img src="img/([a-z0-9-]+)\.jpg"([^>]*)>')


def nav_items(current, items):
    out = []
    for key, href, label in items:
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(out)


def add_srcset(html):
    def repl(m):
        name, rest = m.group(1), m.group(2)
        variants = sorted(
            (p for p in OUT.glob(f"img/{name}-*.webp") if re.fullmatch(rf"{re.escape(name)}-\d+", p.stem)),
            key=lambda p: int(p.stem.rsplit("-", 1)[1]),
        )
        if not variants:
            raise SystemExit(f"no WebP files for img/{name}.jpg; run images.py")
        srcset = ", ".join(f"img/{p.name} {p.stem.rsplit('-', 1)[1]}w" for p in variants)
        if "sizes=" not in rest:
            rest = ' sizes="(max-width: 760px) 100vw, 50vw"' + rest
        return f'<img src="img/{name}.jpg" srcset="{srcset}"{rest}>'
    return IMG.sub(repl, html)


def build():
    built = []
    for src in sorted(PAGES.glob("*.html")):
        text = src.read_text()
        m = re.match(r"<!--\s*(\{.*?\})\s*-->\n", text, re.S)
        if not m:
            raise SystemExit(f"{src.name}: missing JSON front matter")
        meta = json.loads(m.group(1))
        body = text[m.end():]
        current = meta.get("nav", "")
        fill = dict(site=SITE, phone=PHONE, tel=TEL)
        url = f"{SITE_URL}/{'' if src.name == 'index.html' else src.name}" if SITE_URL else ""
        html = HEAD.format(
            title=meta["title"],
            description=meta["description"],
            robots='<meta name="robots" content="noindex">\n' if meta.get("noindex") else "",
            canonical=f'<link rel="canonical" href="{url}">\n' if url else "",
            og_image=f"{SITE_URL}/img/main-street-sign-1200.webp" if SITE_URL else "img/main-street-sign-1200.webp",
            nav=nav_items(current, NAV),
            nav_menu=nav_items(current, [("home", "index.html", "Home")] + NAV + [("book", "book.html", "Book a visit")]),
            book_current=' aria-current="page"' if current == "book" else "",
            **fill,
        )
        html += body
        if meta.get("book", True):
            html += BOOK.format(**fill)
        scripts = "".join(f'<script src="{s}" defer></script>\n' for s in meta.get("scripts", []))
        html += FOOT.format(
            nav_footer=nav_items(None, [("home", "index.html", "Home")] + NAV + [("book", "book.html", "Book a visit")]),
            scripts=scripts,
            **fill,
        )
        head, body_html = html.split("<body>", 1)
        # Keep the phone number on one line wherever it appears as text.
        chunks = re.split(r"(<script.*?</script>)", body_html, flags=re.S)
        body_html = "".join(
            c if c.startswith("<script") else c.replace("(207) 599-6459", '<span class="nw">(207) 599-6459</span>')
            for c in chunks
        )
        (OUT / src.name).write_text(add_srcset(head + "<body>" + body_html))
        if not meta.get("noindex"):
            built.append(src.name)
        print("built", src.name)

    robots = "User-agent: *\nAllow: /\n"
    if SITE_URL:
        urls = "\n".join(f"  <url><loc>{SITE_URL}/{'' if n == 'index.html' else n}</loc></url>" for n in built)
        (OUT / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'
        )
        robots += f"Sitemap: {SITE_URL}/sitemap.xml\n"
    (OUT / "robots.txt").write_text(robots)


if __name__ == "__main__":
    build()
