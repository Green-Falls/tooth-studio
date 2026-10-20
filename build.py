#!/usr/bin/env python3
"""Build the Tooth Studio site: wrap each pages/*.html body in the shared header and footer.

Each page file starts with one line of JSON in an HTML comment:
  <!-- {"title": "...", "description": "...", "nav": "services"} -->
Optional keys: "scripts": ["form.js"],
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

# The contact form posts here. Create a form at formspree.io (or any service that
# accepts a JSON POST and answers {"ok": true}) and paste its URL, for example
# "https://formspree.io/f/abcdwxyz". Left empty, the form says it isn't connected.
FORM_ENDPOINT = ""

SITE = "Tooth Studio & Wellness"
PHONE = "(207) 599-6459"
TEL = "+12075996459"

NAV = [
    ("services", "services.html", "Services"),
    ("whitening", "whitening.html", "Whitening"),
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
<link rel="preload" href="fonts/jost.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/source-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="utility" aria-label="Contact">
    <div class="wrap utility-inner">
      <p class="utility-note"><span class="icon" data-icon="map-pin"></span>55 Main Street, Bridgton <span class="sep" aria-hidden="true">·</span> Taking new patients</p>
      <ul>
        <li><a href="tel:{tel}"><span class="icon" data-icon="phone"></span>Call or text {phone}</a></li>
        <li><a class="utility-cta" href="contact.html#request"><span class="icon" data-icon="calendar-check"></span>Request a visit</a></li>
      </ul>
    </div>
  </nav>
  <div class="wrap masthead">
    <a class="brand" href="index.html"><img src="img/logo.png" alt="{site}, dental hygiene care" width="556" height="158"></a>
    <details class="menu"><summary>Menu</summary><ul>{nav_menu}<li><a href="contact.html#request">Request a visit</a></li><li><a href="tel:{tel}">Call {phone}</a></li></ul></details>
  </div>
  <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap footer-center">
    <img class="footer-logo" src="img/logo.png" alt="{site}" width="556" height="158" loading="lazy">
    <nav aria-label="Footer"><ul class="footer-nav">{nav_footer}</ul></nav>
    <ul class="footer-contact">
      <li><span class="icon" data-icon="map-pin"></span>55 Main Street, 1st floor, Bridgton, ME 04009</li>
      <li><span class="icon" data-icon="phone"></span><a href="tel:{tel}">{phone}</a>, call or text</li>
      <li><span class="icon" data-icon="envelope-simple"></span><a href="mailto:toothstudiomaine@gmail.com">toothstudiomaine@gmail.com</a></li>
    </ul>
    <p class="footer-social"><a href="https://www.facebook.com/profile.php?id=61562688787508">Facebook</a> · <a href="https://www.instagram.com/toothstudioandwellness/">Instagram</a></p>
    <p class="legal">Tooth Studio &amp; Wellness LLC. Rytel Rowe, Independent Practice Dental Hygienist. In network with all Delta Dental plans and MaineCare.</p>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="sms:{tel}"><span class="icon" data-icon="chat-circle-text"></span>Text</a>
  <a href="tel:{tel}"><span class="icon" data-icon="phone"></span>Call</a>
  <a href="contact.html#request"><span class="icon" data-icon="calendar-check"></span>Request</a>
</nav>
{scripts}</body>
</html>
"""

IMG = re.compile(r'<img src="img/([a-z0-9-]+)\.jpg"([^>]*)>')
ICONS = ROOT / "icons"
ICON = re.compile(r'<span class="icon( [^"]*)?" data-icon="([a-z0-9-]+)"></span>')


def add_icons(html):
    def repl(m):
        path = ICONS / f"{m.group(2)}.svg"
        if not path.exists():
            raise SystemExit(f"no icon icons/{m.group(2)}.svg")
        svg = path.read_text().strip().replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
        return f'<span class="icon{m.group(1) or ""}">{svg}</span>'
    return ICON.sub(repl, html)


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
        body = text[m.end():].replace(
            "{form_action}", f'action="{FORM_ENDPOINT}"' if FORM_ENDPOINT else ""
        )
        # House rule: photos never get captions. Review attributions (figures with no image) are fine.
        for fig in re.findall(r"<figure.*?</figure>", body, re.S):
            if "<img" in fig and "<figcaption" in fig:
                raise SystemExit(f"{src.name}: photo has a caption; photos never get captions")
        if "hero-caption" in body:
            raise SystemExit(f"{src.name}: photo caption (hero-caption); photos never get captions")
        current = meta.get("nav", "")
        fill = dict(site=SITE, phone=PHONE, tel=TEL)
        url = f"{SITE_URL}/{'' if src.name == 'index.html' else src.name}" if SITE_URL else ""
        html = HEAD.format(
            title=meta["title"],
            description=meta["description"],
            robots='<meta name="robots" content="noindex">\n' if meta.get("noindex") else "",
            canonical=f'<link rel="canonical" href="{url}">\n' if url else "",
            og_image=f"{SITE_URL}/img/entrance-1200.webp" if SITE_URL else "img/entrance-1200.webp",
            nav=nav_items(current, NAV),
            nav_menu=nav_items(current, [("home", "index.html", "Home")] + NAV),
            **fill,
        )
        html += body
        scripts = "".join(f'<script src="{s}" defer></script>\n' for s in meta.get("scripts", []))
        html += FOOT.format(
            nav_footer=nav_items(None, [("home", "index.html", "Home")] + NAV),
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
        (OUT / src.name).write_text(add_icons(add_srcset(head + "<body>" + body_html)))
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
