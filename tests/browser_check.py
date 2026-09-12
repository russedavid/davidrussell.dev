"""Exercise the actual HTMX runtime against an already-running local server."""

import argparse
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


def check(url, output=None):
    if urlparse(url).hostname not in {"localhost", "127.0.0.1", "::1"}:
        raise ValueError("Use a local server; this check does not exercise production.")
    if output:
        output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for label, width in (("desktop", 1440), ("phone", 390), ("narrow", 320)):
                page = browser.new_page(viewport={"width": width, "height": 900})
                page.route("https://davidrussell-hamburger-or-hotdog.hf.space/**", lambda route: route.fulfill(body="External classifier placeholder"))
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                for name, path in (("home", "/"), ("projects", "/projects"), ("frontline", "/projects/frontline"), ("otsc", "/projects/otsc")):
                    page.goto(url + path, wait_until="networkidle")
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), (label, path)
                    assert page.locator("h1").count() == 1
                    assert page.evaluate("[...document.images].every(i=>i.complete && i.naturalWidth>0)")
                    if output:
                        page.screenshot(path=str(output / f"{name}-{label}.png"), full_page=True)
                page.get_by_role("link", name="2. New requirement").click()
                page.get_by_text("Proposal revised", exact=True).wait_for()
                assert "v is not None" in page.locator(".sample-code").inner_text()
                before = page.locator(".sample-code").inner_text()
                page.get_by_role("link", name="3. No new information").click()
                page.get_by_text("Current output retained", exact=True).wait_for()
                assert before == page.locator(".sample-code").inner_text()
                page.get_by_role("button", name="Use dark theme").click()
                page.goto(url + "/tools", wait_until="domcontentloaded")
                assert page.evaluate("document.documentElement.dataset.theme") == "dark"
                assert page.evaluate("htmx.version") == "4.0.0"
                page.get_by_label("Coordinates (latitude, longitude)").fill("not coordinates")
                page.get_by_label("Google Air Quality API key").fill("test-only-no-provider-call")
                page.get_by_role("button", name="Check Air Quality").click()
                page.get_by_text("Use latitude,longitude:", exact=False).wait_for()
                assert page.url.endswith("/tools")
                assert not errors, errors
                page.close()
                print(f"{label}: pages, layout, theme, walkthrough and HTMX form passed")
            context = browser.new_context(java_script_enabled=False)
            page = context.new_page()
            page.goto(url + "/projects/otsc")
            page.get_by_role("link", name="2. New requirement").click()
            assert page.get_by_text("Proposal revised", exact=True).is_visible()
            context.close()
            print("No-JavaScript walkthrough navigation passed")
        finally:
            browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8017")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    check(args.url.rstrip("/"), args.output)
