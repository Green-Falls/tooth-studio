#!/usr/bin/env python3
"""Build the Tooth Studio site: wrap each pages/*.html body in the shared header and footer.

Each page file starts with one line of JSON in an HTML comment:
  <!-- {"title": "...", "description": "...", "nav": "services"} -->
Output goes to site/<same name>.html. Run: python3 build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
PAGES = ROOT / "pages"
OUT = ROOT / "site"

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
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="img/55-main-street.jpg">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topline"><div class="wrap">
  <span>55 Main Street, 1st floor, Bridgton, Maine</span>
  <span>Call or text <a href="tel:{tel}">{phone}</a></span>
</div></div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html"><img src="img/logo.png" alt="{site}, dental hygiene care" width="556" height="158"></a>
    <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
    <details class="menu"><summary>Menu</summary><ul>{nav_home}{nav}</ul></details>
  </div>
</header>
<main id="main">
"""

BOOK = """<section class="book" aria-label="Book a visit">
  <div class="wrap">
    <div>
      <h2>Book by text or phone</h2>
      <p>Rytel answers texts at {phone}. You can also message the studio on Facebook or Instagram.</p>
    </div>
    <div class="buttons">
      <a class="button primary" href="sms:{tel}">Text {phone}</a>
      <a class="button" href="tel:{tel}">Call</a>
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
          <li><a href="tel:{tel}">{phone}</a> (call or text)</li>
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
</body>
</html>
"""


def nav_items(current, home=False):
    items = [("home", "index.html", "Home")] if home else NAV
    out = []
    for key, href, label in items:
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(out)


def build():
    for src in sorted(PAGES.glob("*.html")):
        text = src.read_text()
        m = re.match(r"<!--\s*(\{.*?\})\s*-->\n", text, re.S)
        if not m:
            raise SystemExit(f"{src.name}: missing JSON front matter")
        meta = json.loads(m.group(1))
        body = text[m.end():]
        current = meta.get("nav", "")
        fill = dict(site=SITE, phone=PHONE, tel=TEL)
        html = HEAD.format(
            title=meta["title"],
            description=meta["description"],
            extra_head=meta.get("head", ""),
            nav=nav_items(current),
            nav_home=nav_items(current, home=True),
            **fill,
        )
        html += body
        if meta.get("book", True):
            html += BOOK.format(**fill)
        html += FOOT.format(nav_footer=nav_items(None, home=True) + nav_items(None), **fill)
        (OUT / src.name).write_text(html)
        print("built", src.name)


if __name__ == "__main__":
    build()
