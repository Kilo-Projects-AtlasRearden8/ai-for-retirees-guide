# STATUS

## What was built

A beginner manual and static HTML site on using free AI in retirement,
published by Asdale Dynamics, LLC.

**Contents**
- `docs/index.md` &mdash; manual overview: what AI is in plain words, how to use
  each guide, large-print reading tips, safety rules, author info
- `docs/staying-connected.md` &mdash; email, video calls, group messages, photo captions
- `docs/hobby-projects.md` &mdash; gardening, crafts, recipes, genealogy, chess
- `docs/health-paperwork.md` &mdash; health summaries, medication schedules,
  appointment trackers, doctor-visit prep, insurance forms (education only,
  not medical advice)
- `docs/travel-planning.md` &mdash; destinations, itineraries, senior discounts,
  packing lists, travel documents
- `docs/scam-avoidance.md` &mdash; common scams aimed at retirees, spotting AI
  fakes, golden rules, safety checklist, what to do if scammed
- `site/` &mdash; static HTML rendering of all six guides:
  `index.html`, `staying-connected.html`, `hobby-projects.html`,
  `health-paperwork.html`, `travel-planning.html`, `scam-avoidance.html`
- `site/css/style.css` &mdash; shared stylesheet, large-print friendly
  (19 px base text, user-scalable, high contrast, print-friendly)
- `site/js/script.js` &mdash; text-size controls persisted in localStorage,
  print button
- `README.md` &mdash; project overview, credits Asdale Dynamics, LLC
- `LICENSE` &mdash; MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `STATUS.md` &mdash; this file

**Style:** plain English, step-by-step checklists, example phrases to copy into
an AI, safety reminders on every guide, large-print friendly, local-first
(static files, no build step, no server required), no secrets or personal data.

## How to run it

No installation or internet is needed to read the files.
1. Open `site/index.html` in any web browser (Chrome, Safari, Edge, Firefox).
2. Use the "Text size" buttons at the top of any page to make text bigger or
   smaller (starts at 19 px; choice is remembered).
3. Click a guide in the navigation bar to read it.
4. Print any page from your browser (Ctrl+P / Command+P); navigation and
   controls are hidden when printing.

To serve over HTTP locally (for testing):
```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/site/index.html
```

## Verification results

All checks passed:
- 6 HTML files parse cleanly (no unclosed tags)
- Every internal link and asset reference resolves to an existing file
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC
- CSS defines a scalable `--base-font-size` starting at 19 px (large print)
- Local HTTP serve test: all 6 pages + CSS + JS returned HTTP 200

No secrets, API keys, or personal data are present in any file.

## Known gaps

- `docs/` (Markdown) and `site/` (HTML) are maintained separately; the HTML is
  not auto-generated from the Markdown, so edits to one side may not reflect in
  the other.
- No automated test suite or linter is configured.
- No site search or sitemap.
- Font-size preference is stored in browser localStorage only (per device,
  not synced).
- Health content is explicitly education only; it is not medical advice.
