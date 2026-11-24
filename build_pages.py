#!/usr/bin/env python3
"""Giacobbe's Italian Restaurant & Pizzeria (Moncks Corner SC) — template v2 T1 build, 2026-11-24, card t_e4ccda17.
Design: letterpress trattoria — Didot-class display / Georgia body, espresso + cream paper +
Naples red + basil, tricolor rules. Distinct from all sibling sites (no phone published: email CTA).
Facts: card-verified + this-run press re-verify ONLY (whatnow.com, Berkeley Observer via SERP,
Holy City Sinner 11-19 tracker, owner FB page live-verified 2026-11-24, Nominatim geo).
No published hours/menu/prices/opening date/phone -> all omitted."""
import os, json, html as H

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
ORIGIN = "https://giacobbe-moncks-corner-demo.up.railway.app"
NAME = "Giacobbe's"
FULL = "Giacobbe's Italian Restaurant & Pizzeria"
ALT = "Giacobbe's Pizzeria & Trattoria"
STREET = "108 W. Railroad Ave"
ADDR = "108 W. Railroad Ave, Moncks Corner, SC 29461"
EMAIL = "giacobbespizza@gmail.com"
FB = "https://www.facebook.com/p/Giacobbes-Pizzeria-Trattoria-61571534981430/"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=108+W.+Railroad+Ave+Moncks+Corner+SC+29461"
LAT, LNG = 33.1928777, -80.0050015
MAPQ = "108+W.+Railroad+Ave%2C+Moncks+Corner%2C+SC+29461"

def canonical(path="/"):
    return ORIGIN + "/" if path == "/" else ORIGIN + path

def ld(objs):
    return "\n".join('<script type="application/ld+json">' + json.dumps(o, separators=(",", ":"), ensure_ascii=False) + "</script>" for o in objs)

def head(path, title, desc, extra_ld=None):
    lds = extra_ld or []
    return f"""<!DOCTYPE html>
<!-- BUILT-2026-11-24 card t_e4ccda17 -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
<meta name="theme-color" content="#17120f">
<link rel="canonical" href="{canonical(path)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{canonical(path)}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{ld(lds)}
</head>"""

NAV = [("/", "Home"), ("/menu", "Menu"), ("/pizzas", "Pizza"), ("/primi-e-secondi", "Kitchen"), ("/visit", "Visit"), ("/contact", "Contact")]

def nav(cur):
    items = []
    for href, label in NAV:
        on = ' aria-current="page"' if href == cur else ""
        cls = ' class="on"' if href == cur else ""
        items.append(f'<a href="{href}"{on}{cls}>{label}</a>')
    return (f'<header class="top"><div class="wrap bar">'
            f'<a class="brand" href="/"><span class="dot" aria-hidden="true"></span>{NAME}</a>'
            f'<nav aria-label="Main">{"".join(items)}</nav>'
            f'<a class="pill mail" href="mailto:{EMAIL}">Email us</a>'
            f'</div><div class="tricolor" aria-hidden="true"></div></header>')

def foot():
    return f"""<footer class="foot"><div class="wrap footgrid">
<div><p class="fbrand">{NAME}</p><p class="ftag">Bacoli &mdash; Napoli &mdash; Moncks Corner</p></div>
<div class="footcol"><p>{STREET}<br>Moncks Corner, SC 29461</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="{FB}" rel="nofollow">Follow the opening on Facebook</a></p></div>
<nav class="footnav" aria-label="Footer">{" ".join(f'<a href="{h}">{l}</a>' for h, l in NAV if h != "/")} <a href="/privacy">Privacy</a></nav>
</div><p class="footline"><span>&copy; 2026 {FULL}, Moncks Corner, South Carolina</span></p></footer>"""

def page(path, title, desc, body, extra_ld=None, cur="/"):
    skip = '<a class="skip" href="#main">Skip to main content</a>\n'
    return (head(path, title, desc, extra_ld) + "\n<body>\n" + skip + nav(cur) + "\n<main id=\"main\">\n" + body + "\n</main>\n" + foot() + "\n</body>\n</html>\n")

def crumbs(*items):
    nodes = [{"@type": "ListItem", "position": i + 1, "name": n, "item": canonical(p)} for i, (n, p) in enumerate(items)]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": nodes}

FAQ_LDS = lambda qs: {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}

BUSINESS = {
    "@context": "https://schema.org", "@type": "Restaurant", "name": FULL, "alternateName": ALT,
    "image": ORIGIN + "/og.png", "url": ORIGIN, "hasMenu": canonical("/menu"),
    "servesCuisine": ["Italian", "Pizza"],
    "address": {"@type": "PostalAddress", "streetAddress": "108 W. Railroad Ave (State Rd S-8-245)",
                "addressLocality": "Moncks Corner", "addressRegion": "SC", "postalCode": "29461", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
    "hasMap": MAPS_LINK,
}
SVC_PROVIDER = {"@type": "Restaurant", "name": FULL, "address": BUSINESS["address"]}

def svc_ld(name, desc):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
            "serviceType": "Restaurant", "provider": SVC_PROVIDER,
            "areaServed": {"@type": "Place", "name": "Moncks Corner, South Carolina"}}

MENU_LD = {
    "@context": "https://schema.org", "@type": "Menu", "name": "What's coming at Giacobbe's", "inLanguage": "en-US",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "Pizza", "description": "New York-style slices and pies, Sicilian-style trays, and a wood-fired oven night once a week."},
        {"@type": "MenuSection", "name": "Pasta", "description": "Homemade pastas, with the family sauce recipe carried from Bacoli, near Naples."},
        {"@type": "MenuSection", "name": "Seafood & Steaks", "description": "Secondi plates — seafood and steaks — the way an Italian dinner goes."},
        {"@type": "MenuSection", "name": "Bar", "description": "A full bar alongside dinner."},
        {"@type": "MenuSection", "name": "Lunch Specials", "description": "Generous lunch specials."},
    ],
}

# ---------------- page bodies ----------------

HOME = """<section class="hero"><div class="wrap herogrid">
<div class="herotext">
<p class="kicker">Opening soon &middot; Downtown Moncks Corner</p>
<h1>{name}&rsquo;</h1>
<p class="sub">Trattoria &bull; Pizzeria &bull; Bar</p>
<p class="lede">Ciao! A family Italian restaurant from Bacoli — the town near Naples — landing at {addr}. New York- and Sicilian-style pizza, pasta made the old way, seafood and steaks. The opening date is coming — everything else is ready.</p>
<div class="ctarow"><a class="pill big" href="/contact">Email the shop</a><a class="pill ghost" href="/menu">See what&rsquo;s coming</a></div>
</div>
<div class="heroplate" aria-hidden="true"><div class="plate"><span class="pG">G</span><span class="pcity">Moncks Corner &middot; South Carolina</span><span class="paddr">{street}</span></div></div>
</div></section>

<section class="sec"><div class="wrap">
<p class="eyebrow">The plan for Railroad Ave</p>
<div class="cards">
<article class="card"><span class="num">I</span><h2>The pizza</h2><p>New York-style slices, Sicilian-style trays — and a wood-fired oven night once a week.</p><p class="more"><a href="/pizzas">All about the pizza &rarr;</a></p></article>
<article class="card"><span class="num">II</span><h2>The kitchen</h2><p>Homemade pastas, seafood and steaks — recipes carried from Bacoli, where the family grew up cooking.</p><p class="more"><a href="/primi-e-secondi">Primi &amp; secondi &rarr;</a></p></article>
<article class="card"><span class="num">III</span><h2>The room</h2><p>A proper dining room with a bar — plus an outdoor area with benches and room for kids to play.</p><p class="more"><a href="/menu">The full menu ahead &rarr;</a></p></article>
</div>
</div></section>

<section class="story"><div class="wrap narrow">
<p class="eyebrow">From Bacoli to Moncks Corner</p>
<h2>A family story, two towns</h2>
<p>Giacobbe Scotto grew up in Bacoli, less than 13 miles from Naples, in a house where his father made a whole year of tomato sauce in Italy before opening his own restaurant. Rachel — his wife and partner — grew up right here in Moncks Corner. When the two decided the time had come to open their own place, they chose her hometown: the small town they both fell in love with, and one of its most recognizable old buildings, at 108 W. Railroad Ave.</p>
<p>The goal, in Giacobbe&rsquo;s own words, is <em>true restaurant dining</em> — brought to a town he believes is hungry for it.</p>
</div></section>

<section class="band"><div class="wrap narrow">
<p class="eyebrow gold">It&rsquo;s happening soon</p>
<blockquote>&ldquo;Things are finally starting to move the right direction. I don&rsquo;t want to spoil any dates yet but it&rsquo;s happening soon! Thank you for the interest, looking forward to meeting you. Ciao!&rdquo;</blockquote>
<p class="who">— Giacobbe, on the shop&rsquo;s Facebook page</p>
<div class="ctarow"><a class="pill big" href="{fb}" rel="nofollow">Follow on Facebook</a><a class="pill outline" href="/contact">Get an email when we open</a></div>
</div></section>

<section class="sec faq"><div class="wrap narrow">
<p class="eyebrow">Questions folks keep asking</p>
<h2>Good to know</h2>
<div itemscope itemtype="https://schema.org/FAQPage">
<div class="qa"><p class="q">When does Giacobbe&rsquo;s open?</p><p class="a">The opening date isn&rsquo;t set yet — when it is, it lands on the shop&rsquo;s <a href="{fb}" rel="nofollow">Facebook page</a> first. Leave a note on our <a href="/contact">contact page</a> and the team will write you.</p></div>
<div class="qa"><p class="q">What kind of pizza do you make?</p><p class="a">Both New York-style and Sicilian-style — plus a wood-fired oven night once a week. <a href="/pizzas">More about the pizza</a>.</p></div>
<div class="qa"><p class="q">Where exactly are you?</p><p class="a">108 W. Railroad Ave (State Rd S-8-245), downtown Moncks Corner, SC 29461 — <a href="/visit">visit page with map</a>.</p></div>
<div class="qa"><p class="q">Are kids and groups welcome?</p><p class="a">The plan includes an outdoor area with benches and room for kids to play. Group and event notes are welcome by email.</p></div>
</div>
</div></section>

<section class="strip"><div class="wrap stripg">
<div><p class="eyebrow">Find us when we open</p><p class="bigaddr">{addr}</p><p class="fine">Hours and opening date announced soon.</p></div>
<div class="ctarow"><a class="pill big" href="{maps}">Open in Google Maps</a><a class="pill outline" href="/visit">Getting-here details</a></div>
</div></section>
""".format(name=NAME, addr=ADDR, street=STREET, fb=FB, maps=MAPS_LINK)

MENU = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">The menu ahead</p>
<h1>What the kitchen is bringing</h1>
<p class="lede">Everything on this page is what the owners have told the local press about the opening menu — nothing is invented. The full menu, with prices, arrives the week the doors open.</p>
</div></section>

<section class="sec"><div class="wrap"><div class="board">
<div class="ms"><p class="msname">Pizza</p><p>New York-style slices and whole pies, Sicilian-style trays, and a wood-fired oven night once a week.</p><p class="more"><a href="/pizzas">The pizza page &rarr;</a></p></div>
<div class="ms"><p class="msname">Pasta</p><p>Homemade pastas, made the old way — with the family&rsquo;s sauce recipe from Bacoli, where Giacobbe&rsquo;s father made a whole year of tomato sauce by hand.</p><p class="more"><a href="/primi-e-secondi">Primi &amp; secondi &rarr;</a></p></div>
<div class="ms"><p class="msname">Seafood &amp; Steaks</p><p>The big plates — seafood and steaks — served the way an Italian dinner goes: first the pasta, then the main.</p><p class="more"><a href="/primi-e-secondi">Primi &amp; secondi &rarr;</a></p></div>
<div class="ms"><p class="msname">Bar</p><p>A full bar alongside dinner — an Italian tradition this place isn&rsquo;t skipping.</p></div>
<div class="ms"><p class="msname">Lunch Specials</p><p>Generous lunch specials, so midday counts too.</p></div>
</div></div></section>

<section class="band"><div class="wrap narrow">
<p class="eyebrow gold">Want the first word?</p>
<p>The team reads every message. Ask a question about the menu, a future booking, or just say ciao.</p>
<div class="ctarow"><a class="pill big" href="/contact">Email the shop</a><a class="pill outline" href="{fb}" rel="nofollow">Follow on Facebook</a></div>
</div></section>
""".format(fb=FB)

PIZZAS = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">The headline</p>
<h1>New York-style and Sicilian-style</h1>
<p class="lede">Two pizza traditions, one kitchen — and a wood-fired oven that comes out once a week.</p>
</div></section>

<section class="sec"><div class="wrap narrow">
<div class="ms"><p class="msname">New York-style</p><p>The big, thin pie — cut in slices, meant for folding. Dinner tonight, no planning needed.</p></div>
<div class="ms"><p class="msname">Sicilian-style</p><p>Thick, fluffy and baked in a tray, cut into squares — the style of Italy&rsquo;s island south-west of Naples, not far from where the family is from.</p></div>
<div class="ms"><p class="msname">Once a week, wood-fired</p><p>One night a week the kitchen fires the wood oven for a limited run of pies. Follow the shop&rsquo;s <a href="{fb}" rel="nofollow">Facebook page</a> — those nights get announced there.</p></div>
<p class="fine">Slices, whole pies and lunch specials — the exact menu and prices land opening week.</p>
<div class="ctarow"><a class="pill big" href="/contact">Email the shop</a><a class="pill outline" href="/menu">Back to the menu</a></div>
</div></section>
""".format(fb=FB)

PRIMI = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">Primi e secondi</p>
<h1>Pasta, seafood and steaks</h1>
<p class="lede">A trattoria menu runs in courses — the pasta comes first, then the big plates. That&rsquo;s the shape of dinner at Giacobbe&rsquo;s.</p>
</div></section>

<section class="sec"><div class="wrap narrow">
<div class="ms"><p class="msname">Primi — homemade pasta</p><p>Pastas made in house, the old way. The sauce recipe is the family&rsquo;s: Giacobbe&rsquo;s father made a whole year of tomato sauce by hand in Bacoli before he ever opened his own restaurant.</p></div>
<div class="ms"><p class="msname">Secondi — seafood &amp; steaks</p><p>Seafood and steaks, cooked Italian-style. The menu details arrive opening week.</p></div>
<div class="ms"><p class="msname">Dolci</p><p>Dinner should end with something sweet — expect them on the menu.</p></div>
<p class="fine">True restaurant dining means courses, not counter food — that&rsquo;s the idea behind this menu.</p>
<div class="ctarow"><a class="pill big" href="/contact">Email the shop</a><a class="pill outline" href="/menu">Back to the menu</a></div>
</div></section>"""

VISIT = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">Visit</p>
<h1>108 W. Railroad Ave</h1>
<p class="lede">Downtown Moncks Corner — one of the town&rsquo;s most recognizable old buildings, under careful renovation, keeping the historic look downtown loves.</p>
</div></section>

<section class="sec"><div class="wrap mapwrap">
<iframe title="Map to Giacobbe&rsquo;s at 108 W. Railroad Ave, Moncks Corner, South Carolina" src="https://maps.google.com/maps?q={mapq}&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div></section>

<section class="sec"><div class="wrap visitg">
<div><p class="eyebrow">The address</p>
<p class="bigaddr">{street} (State Rd S-8-245)<br>Moncks Corner, SC 29461</p>
<p class="fine">Opening date and hours: to be announced — they land on the shop&rsquo;s Facebook page first.</p>
<div class="ctarow"><a class="pill big" href="{maps}">Open in Google Maps</a><a class="pill outline" href="/contact">Email the shop</a></div></div>
<div class="visitcard"><p class="eyebrow gold">Before the doors open</p>
<p>Questions about the building, the timeline, groups or future bookings — the team answers email today: <a href="mailto:{email}">{email}</a>.</p>
<p><a class="fb" href="{fb}" rel="nofollow">Follow the build on Facebook &rarr;</a></p></div>
</div></section>
""".format(mapq=MAPQ, street=STREET, maps=MAPS_LINK, email=EMAIL, fb=FB)

CONTACT = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">Contact</p>
<h1>Talk to the shop</h1>
<p class="lede">Email is the fastest way to reach the team today: <a href="mailto:{email}">{email}</a>. Or leave a note here — it lands in the same inbox.</p>
</div></section>

<section class="sec"><div class="wrap formwrap">
<form class="cform" method="post" action="/contact">
<div class="frow"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" maxlength="120" required autocomplete="name"></div>
<div class="frow"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel"></div>
<div class="frow"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" maxlength="120" autocomplete="email"></div>
<div class="frow"><label for="f-msg">What do you need?</label><textarea id="f-msg" name="message" rows="6" maxlength="4000" required placeholder="e.g. Are you taking group bookings for when you open? We&rsquo;d love ten people for a Sicilian night."></textarea></div>
<button class="pill big" type="submit">Send to the shop</button>
</form>
<aside class="cside">
<p class="eyebrow gold">Other ways</p>
<p>Email: <a href="mailto:{email}">{email}</a></p>
<p>Facebook: <a href="{fb}" rel="nofollow">{name} on Facebook</a></p>
<p class="fine">Email gets answered fastest right now — before opening, it&rsquo;s how the team talks to the town.</p>
</aside>
</div></section>
""".format(email=EMAIL, fb=FB, name=NAME)

PRIVACY = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">Privacy</p>
<h1>How this site treats your note</h1>
</div></section>

<section class="sec"><div class="wrap narrow">
<h2>What gets collected</h2>
<p>This site collects only what you type into the contact form — your name, and optionally your phone and email, plus your message. The form sends that note to the shop&rsquo;s inbox so the team can answer you.</p>
<h2>Who runs the site</h2>
<p>The site was built for {full} of {addr}. Questions about this site: <a href="mailto:{email}">{email}</a>.</p>
<h2>No trackers</h2>
<p>No advertising pixels, no third-party analytics, no cookies set by this site beyond what a normal web browser keeps. The map on the visit page is a Google Maps embed; Google may see your IP when it loads.</p>
<h2>Questions</h2>
<p>Write to <a href="mailto:{email}">{email}</a> and ask whoever handles the website.</p>
</div></section>
""".format(full=FULL, addr=ADDR, email=EMAIL)

THANKS = """<section class="phead sent"><div class="wrap narrow">
<p class="eyebrow gold">Sent</p>
<h1>Your note is on its way to {name}&rsquo;s</h1>
<p class="lede">The team reads every message — expect a reply by email. Prefer to write direct? <a href="mailto:{email}">{email}</a>.</p>
<div class="ctarow"><a class="pill big" href="/">Back to home</a><a class="pill outline" href="/menu">See what&rsquo;s coming</a></div>
</div></section>
""".format(name=NAME, email=EMAIL)

FOUROFOUR = """<section class="phead"><div class="wrap narrow">
<p class="eyebrow">404</p>
<h1>That page isn&rsquo;t here — yet.</h1>
<p class="lede">Like the restaurant, some parts of this site are still opening. Try one of these:</p>
<div class="ctarow"><a class="pill big" href="/">Home</a><a class="pill outline" href="/menu">The menu ahead</a><a class="pill outline" href="/visit">Visit</a><a class="pill outline" href="/contact">Contact</a></div>
</div></section>"""

# ---------------- assemble ----------------

pages_written = []
def W(fname, path, title, desc, body, lds=None, cur="/"):
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(page(path, title, desc, body, lds, cur))
    pages_written.append(path)

W("index.html", "/", "Giacobbe's Italian Restaurant & Pizzeria — Opening Soon in Downtown Moncks Corner, SC",
  "A family Italian restaurant from Bacoli, near Naples — NY- and Sicilian-style pizza, pasta, seafood and steaks — opening soon at 108 W. Railroad Ave, Moncks Corner, SC 29461.",
  HOME, [BUSINESS, FAQ_LDS([
    ("When does Giacobbe's open?", "The opening date isn't set yet — when it is, it lands on the shop's Facebook page first. Leave a note on the contact page and the team will write you."),
    ("What kind of pizza do you make?", "Both New York-style and Sicilian-style — plus a wood-fired oven night once a week."),
    ("Where exactly are you?", "108 W. Railroad Ave (State Rd S-8-245), downtown Moncks Corner, SC 29461."),
    ("Are kids and groups welcome?", "The plan includes an outdoor area with benches and room for kids to play. Group and event notes are welcome by email.")])])
W("menu.html", "/menu", "The Menu Ahead — Giacobbe's Italian Restaurant & Pizzeria, Moncks Corner SC",
  "What Giacobbe's will serve at opening: NY- and Sicilian-style pizza, wood-fired nights, homemade pasta, seafood, steaks, a bar and lunch specials. Prices land opening week.",
  MENU, [MENU_LD, crumbs(("Home", "/"), ("Menu", "/menu"))], cur="/menu")
W("pizzas.html", "/pizzas", "New York- & Sicilian-Style Pizza — Giacobbe's Pizzeria, Moncks Corner SC",
  "New York-style slices and Sicilian-style trays, plus a wood-fired oven night once a week — from Giacobbe's, opening soon in downtown Moncks Corner, SC.",
  PIZZAS, [svc_ld("New York- & Sicilian-Style Pizza", "New York-style slices and pies, Sicilian-style trays, and a wood-fired oven night once a week."),
           crumbs(("Home", "/"), ("Menu", "/menu"), ("Pizza", "/pizzas"))], cur="/pizzas")
W("primi-e-secondi.html", "/primi-e-secondi", "Pasta, Seafood & Steaks — Giacobbe's Trattoria, Moncks Corner SC",
  "Homemade pastas, seafood and steaks served in proper courses at Giacobbe's Trattoria, opening soon at 108 W. Railroad Ave, Moncks Corner, SC.",
  PRIMI, [svc_ld("Pasta, Seafood & Steaks", "Homemade pastas plus seafood and steak secondi plates, served Italian-style in courses."),
          crumbs(("Home", "/"), ("Menu", "/menu"), ("Kitchen", "/primi-e-secondi"))], cur="/primi-e-secondi")
W("visit.html", "/visit", "Visit 108 W. Railroad Ave — Giacobbe's, Downtown Moncks Corner SC",
  "108 W. Railroad Ave (State Rd S-8-245), downtown Moncks Corner, SC 29461 — opening soon. Hours and opening date announced on the shop's Facebook page.",
  VISIT, [crumbs(("Home", "/"), ("Visit", "/visit"))], cur="/visit")
W("contact.html", "/contact", "Contact Giacobbe's Italian Restaurant & Pizzeria — Moncks Corner SC",
  "Email giacobbespizza@gmail.com or leave a note — the team behind Giacobbe's answers every message. Opening soon in Moncks Corner, SC.",
  CONTACT, [crumbs(("Home", "/"), ("Contact", "/contact"))], cur="/contact")
W("privacy.html", "/privacy", "Privacy — Giacobbe's, Moncks Corner SC",
  "How this site handles your contact-form note: it goes straight to the shop's inbox. No trackers, no third-party analytics. Giacobbe's, Moncks Corner SC.",
  PRIVACY, [crumbs(("Home", "/"), ("Privacy", "/privacy"))], cur="/privacy")
W("thanks.html", "/thanks", "Message Sent — Giacobbe's, Moncks Corner SC",
  "Your note just landed in Giacobbe's inbox. The team reads every message — expect a reply soon.",
  THANKS, None, cur="/")
W("404.html", "/404", "Page Not Found — Giacobbe's, Moncks Corner SC",
  "This page isn't on the site yet — like the restaurant, still opening. Giacobbe's, Moncks Corner SC.",
  FOUROFOUR, None, cur="/")

# sitemap + robots
today = "2026-11-24"
core = ["/", "/menu", "/pizzas", "/primi-e-secondi", "/visit", "/contact", "/privacy"]
urls = "\n".join(f'  <url><loc>{canonical(p)}</loc><lastmod>{today}</lastmod></url>' for p in core)
open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\nDisallow: /thanks\nDisallow: /404\n\nSitemap: " + ORIGIN + "/sitemap.xml\n")

print("wrote:", ", ".join(pages_written), "+ sitemap.xml + robots.txt")
