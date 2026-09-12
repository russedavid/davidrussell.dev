# davidrussell.dev

David Russell's personal website: projects, writing, and a few small tools. Built with FastHTML and server-rendered HTML, with a beige default theme and an optional warm dark theme.

## Run locally

Tested with Python 3.13. The application requires Python 3.10 or newer.

```sh
uv venv --python 3.13
uv pip install -r requirements.txt
.venv/bin/python main.py
```

Open the localhost address printed by the server. Alternatively:

```sh
.venv/bin/python -m uvicorn main:app --host 127.0.0.1 --port 8017 --reload
```

The site needs no application API keys, database, or login. The air-quality tool accepts a visitor's Google Air Quality API key for that request; its form uses POST and provider errors do not echo the key. The classifier remains an externally hosted Hugging Face iframe.

## Stack

Checked September 12, 2026:

| Component | Version |
|---|---|
| python-fasthtml | 0.14.13 |
| HTMX | 4.0.0, through `FastHTML(htmx4=True)` |
| Pico CSS | 2.1.1 |
| Uvicorn | 0.52.4 |
| Requests | 2.34.2 |

[HTMX 4](https://four.htmx.org/docs/) is selected explicitly: npm's `latest` tag still points to the 2.x line. Pico is the site's styling foundation; MonsterUI is not needed here. Source Serif 4 and Source Sans 3 are served locally, with their licenses in `public/fonts/`.

The application has no session middleware. Static serving is restricted to `public/`; local session files, Python sources, and development artifacts are not web assets.

## Project pages

- **Frontline**: `/projects/frontline`, with the public demo, source repository, a clearly labeled report illustration, and links to evaluation work.
- **Over The Shoulder Coder**: `/projects/otsc`, with the product story and an interactive, fixed-example walkthrough. It is an illustration, not a running desktop app or live inference endpoint. OTSC's source repository and recorded evaluations remain private.

Project descriptions and sample content live in `projects.py`. `main.py` owns routes and layout, `styles.py` supplies the theme, and `public/site.js` persists the theme preference. Blog content remains in `blogs.py`.

## Checks

The server checks use mocked provider responses and make no paid API requests:

```sh
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
uv pip check --python .venv/bin/python
```

For browser checks, install the optional development requirements and start the local server:

```sh
uv pip install -r requirements-dev.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python tests/browser_check.py --url http://127.0.0.1:8017
```

The browser check covers desktop and phone layouts, theme persistence, real HTMX 4 form submission, walkthrough navigation, and navigation with JavaScript disabled. Pass `--output /tmp/davidrussell-site-review` to save review screenshots outside the repository. The classifier iframe is stubbed during the check; air-quality inputs are intentionally invalid so no Google request is made.

## Deployment

The existing Vercel project is connected to this repository. Pushing `main` triggers its configured deployment. The ASGI application is exported as `main:app`; importing it does not start a development server or write a session key.

Vercel serves public assets separately from the Python function. The app mounts `public/` only when that directory exists, so local asset serving works without making deployment startup depend on it.

Keep `.vercel/`, `.env*`, `.sesskey`, caches, and review output out of Git. The site refresh was checked locally; the owner is handling verification of the live deployment.
