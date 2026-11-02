# Free AI for Retirement

A beginner-friendly manual and static website for using free artificial
intelligence in retirement: staying connected, hobby projects, health paperwork,
travel planning, and scam avoidance. Written in plain English, with large-print
friendly design and step-by-step checklists.

Published by **Asdale Dynamics, LLC** (Indiana, formed October 2026), founded by
Dylan Asdale, a registered nurse turned AI author. Dylan writes AI guides "like
a friend would": plain English, step by step, never condescending. More of his
work is at dylanasdale.github.io.

## What is inside

| Folder | Contents |
|--------|----------|
| `docs/` | Markdown source manuals: index, Staying Connected, Hobby Projects, Health Paperwork, Travel Planning, Scam Avoidance |
| `site/` | Static HTML site: 6 pages, one shared stylesheet, and a font-size helper script |
| `scripts/verify_site.py` | Automated verification: parses HTML, checks every link and asset, confirms the LICENSE and README credits |
| `LICENSE` | MIT License &mdash; Copyright (c) 2026 Asdale Dynamics, LLC |
| `STATUS.md` | What was built, how to run it, verification results, known gaps |

## Topics

- **Staying Connected** &mdash; email, video calls, group messages, photo captions
- **Hobby Projects** &mdash; gardening, crafts, recipes, genealogy, chess
- **Health Paperwork** &mdash; health summaries, medication schedules, appointment trackers, doctor-visit prep (education only, not medical advice)
- **Travel Planning** &mdash; destinations, itineraries, senior discounts, packing lists
- **Scam Avoidance** &mdash; spotting AI voice scams, fake emails, and what to do if scammed

## How to use it

No installation or internet connection is needed to read the files.

1. Open `site/index.html` in any web browser (Chrome, Safari, Edge, Firefox).
2. Use the "Text size" buttons at the top of any page to make the text bigger or
   smaller. It starts at 19 px (large-print friendly) and your choice is remembered.
3. Work through a guide's checklist one step at a time. There is no rush.
4. Print any page from your browser (Ctrl+P / Command+P). Navigation and controls
   are hidden when printing.

To serve the site over HTTP locally:
```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/site/index.html
```

## Who this is for

Beginners, especially retirees, who want plain-English, step-by-step help with
free AI tools. No prior AI or computer expertise is assumed beyond opening a web
browser.

## Style

Clear, warm, polished, tested, local-first. No secrets, API keys, or personal
data are included in this repository.

## Safety

- Never share passwords, Social Security numbers, credit card numbers, or your
  full home address with an AI tool.
- The health paperwork guide is education only &mdash; not medical advice.
  Always talk with your doctor or nurse about health decisions.
- See the Scam Avoidance guide for how to spot AI-generated scams.

## Run the verification

```
python3 scripts/verify_site.py
```

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## Credits

Written and published by Asdale Dynamics, LLC.
