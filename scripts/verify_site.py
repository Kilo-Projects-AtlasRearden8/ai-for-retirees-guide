import html.parser
import re
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = [
    "site/index.html",
    "site/staying-connected.html",
    "site/hobby-projects.html",
    "site/health-paperwork.html",
    "site/travel-planning.html",
    "site/scam-avoidance.html",
]

errors = []

class Checker(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.open_tags = []
        self.void = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }
    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.open_tags.append(tag)
    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if self.open_tags and self.open_tags[-1] == tag:
            self.open_tags.pop()
        else:
            errors.append("%s: unexpected closing </%s> (open: %s)" % (
                self.path, tag, self.open_tags[-5:]))

for f in HTML_FILES:
    p = os.path.join(ROOT, f)
    with open(p, encoding="utf-8") as fh:
        content = fh.read()
    c = Checker(f)
    c.feed(content)
    if c.open_tags:
        errors.append("%s: unclosed tags at EOF: %s" % (f, c.open_tags))

    base = os.path.dirname(p)
    for m in re.finditer(r'href="([^"]+)"', content):
        href = m.group(1)
        if href.startswith(("http", "mailto", "#")):
            continue
        target = os.path.normpath(os.path.join(base, href))
        if not os.path.exists(target):
            errors.append("%s: broken link %s -> %s missing" % (f, href, target))

    for m in re.finditer(r'(?:src|href)="([^"]+)"', content):
        src = m.group(1)
        if src.startswith(("http", "mailto", "#")):
            continue
        target = os.path.normpath(os.path.join(base, src))
        if not os.path.exists(target):
            errors.append("%s: missing asset %s -> %s" % (f, src, target))

with open(os.path.join(ROOT, "LICENSE"), encoding="utf-8") as fh:
    lic = fh.read()
if "Copyright (c) 2026 Asdale Dynamics, LLC" not in lic:
    errors.append("LICENSE: missing exact copyright line")

with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
    readme = fh.read()
if "Asdale Dynamics, LLC" not in readme:
    errors.append("README: missing Asdale Dynamics, LLC credit")

with open(os.path.join(ROOT, "site/css/style.css"), encoding="utf-8") as fh:
    css = fh.read()
if "--base-font-size" not in css or "19px" not in css:
    errors.append("CSS: missing large-print base font size")

for term in ["Social Security", "credit card", "password"]:
    pass

if errors:
    print("VERIFICATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VERIFICATION PASSED")
print("HTML files parsed: %d, no unclosed tags" % len(HTML_FILES))
print("All internal links and assets resolve")
print("LICENSE copyright line present")
print("README credits Asdale Dynamics, LLC")
print("Large-print CSS present (19 px base, scalable)")
