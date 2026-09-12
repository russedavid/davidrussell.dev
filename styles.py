"""The site's warm, responsive light and dark themes."""

BASE_STYLES = """
@font-face { font-family: 'Source Sans'; src: url('/public/fonts/source-sans/SourceSans3-Regular.otf') format('opentype'); font-weight: 400; font-display: swap; }
@font-face { font-family: 'Source Sans'; src: url('/public/fonts/source-sans/SourceSans3-Semibold.otf') format('opentype'); font-weight: 600 900; font-display: swap; }
@font-face { font-family: 'Source Serif'; src: url('/public/fonts/source-serif/SourceSerif4-Regular.otf') format('opentype'); font-weight: 400; font-display: swap; }
@font-face { font-family: 'Source Serif'; src: url('/public/fonts/source-serif/SourceSerif4-Semibold.otf') format('opentype'); font-weight: 600 900; font-display: swap; }
:root, [data-theme=light] {
    color-scheme: light;
    --background: #f5efe4; --surface: #fcf8f1; --highlight: #ebe1d2;
    --text: #33291f; --muted: #6c5c4d; --accent: #815435; --accent-hover: #5e3921;
    --border: #d7c8b5; --strong-border: #b2997e; --code-bg: #efe6d8;
    --success: #496044; --error: #9b342a;
    --pico-font-family: 'Source Sans', system-ui, sans-serif;
    --pico-font-size: 18px; --pico-line-height: 1.65;
    --pico-background-color: var(--background); --pico-color: var(--text);
    --pico-primary: var(--accent); --pico-primary-hover: var(--accent-hover);
    --pico-primary-background: var(--accent); --pico-primary-hover-background: var(--accent-hover);
    --pico-primary-border: var(--accent); --pico-primary-hover-border: var(--accent-hover);
    --pico-primary-inverse: #fffaf3; --pico-primary-focus: #81543533;
    --pico-muted-color: var(--muted); --pico-muted-border-color: var(--border);
    --pico-card-background-color: var(--surface); --pico-card-border-color: var(--border);
    --pico-form-element-background-color: var(--surface); --pico-form-element-color: var(--text);
    --pico-form-element-border-color: var(--strong-border); --pico-form-element-placeholder-color: var(--muted);
    --pico-border-radius: 6px;
}
[data-theme=dark] {
    color-scheme: dark;
    --background: #241f1a; --surface: #2e2721; --highlight: #3c3026;
    --text: #f3e9db; --muted: #c4b5a3; --accent: #ddb58e; --accent-hover: #f4cfaa;
    --border: #544637; --strong-border: #91775c; --code-bg: #201b16;
    --success: #b3c899; --error: #f0a293;
    --pico-primary-background: #a5734c; --pico-primary-hover-background: #91603e;
    --pico-primary-inverse: #fffaf3; --pico-primary-focus: #ddb58e44;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 32px; }
body { margin: 0; background: var(--background); color: var(--text); min-height: 100vh; }
h1,h2,h3,h4 { color: var(--text); font-family: 'Source Serif', Georgia, serif; font-weight: 400; line-height: 1.12; text-wrap: balance; }
h1 { font-size: clamp(2.5rem, 5vw, 4.5rem); letter-spacing: -.045em; margin-bottom: 1.4rem; }
h2 { font-size: clamp(1.8rem, 3vw, 2.6rem); letter-spacing: -.035em; }
h3 { font-size: 1.45rem; letter-spacing: -.02em; }
p { margin-bottom: 1.2rem; }
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: .2em; }
a:hover { color: var(--accent-hover); }
a:focus-visible,button:focus-visible,summary:focus-visible { outline: 3px solid var(--accent); outline-offset: 5px; }
button { font-family: inherit; }
.site-width { width: min(1160px, calc(100% - 96px)); margin-inline: auto; }
.site-header { border-bottom: 1px solid var(--border); }
.site-nav { min-height: 96px; display: flex; align-items: center; justify-content: space-between; gap: 2rem; }
.brand { font-family: 'Source Serif', Georgia, serif; font-size: 1.6rem; color: var(--text); text-decoration: none; letter-spacing: -.08em; }
.nav-links { display: flex; align-items: center; gap: 1.9rem; }
.nav-item { color: var(--muted); text-decoration: none; font-size: .85rem; }
.nav-item:hover,.nav-item.active { color: var(--text); }
.nav-item.active { text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: .55em; }
.theme-toggle { display: inline-flex; align-items: center; gap: .4rem; width: auto; padding: .3rem .7rem; margin: 0; color: var(--text); background: transparent; border: 1px solid var(--border); font-size: .78rem; box-shadow: none; }
.theme-toggle:hover { background: var(--highlight); border-color: var(--strong-border); }
.skip-link { position: absolute; left: 1rem; top: -100px; z-index: 10; background: var(--surface); padding: .7rem 1rem; }
.skip-link:focus { top: 1rem; }
.site-main { padding-block: 64px 72px; min-height: 65vh; }
.eyebrow { font: 600 .7rem/1.5 'Source Sans', sans-serif; letter-spacing: .17em; text-transform: uppercase; color: var(--muted); margin-bottom: 1rem; }
.hero-section { display: grid; grid-template-columns: 1.5fr 1fr; gap: 5rem; align-items: center; padding: 12px 0 68px; }
.hero-title { font-size: clamp(3rem, 6.5vw, 5.1rem); margin-bottom: 1.4rem; }
.hero-subtitle { max-width: 560px; font-size: 1.25rem; line-height: 1.55; color: var(--muted); }
.hero-portrait { margin: 0; justify-self: end; width: min(100%, 315px); }
.hero-image { width: 100%; height: 335px; object-fit: cover; object-position: center 38%; border-radius: 3px; }
.hero-portrait figcaption { font-size: .72rem; color: var(--muted); margin-top: .7rem; padding: 0; }
.actions { display: flex; flex-wrap: wrap; align-items: center; gap: 1.2rem; margin: 1.6rem 0 0; }
.button-link { display: inline-flex; align-items: center; justify-content: center; gap: .6rem; padding: .65rem 1.05rem; background: var(--accent); color: var(--background); font-size: .9rem; font-weight: 600; text-decoration: none; border: 1px solid var(--accent); border-radius: 4px; }
.button-link:hover { background: var(--accent-hover); color: var(--background); }
.text-link { font-size: .9rem; font-weight: 600; }
.section-heading { display: flex; justify-content: space-between; gap: 1.5rem; align-items: baseline; margin: 0 0 1.6rem; }
.section-heading h2 { margin: 0; }
.interests { border-top: 1px solid var(--border); padding-top: 2rem; margin-top: 2.8rem; }
.interest-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; }
.interest-grid h3 { margin-bottom: .9rem; }
.interest-grid p { color: var(--muted); }
.blog-date { color: var(--muted); font-size: .8rem; margin-bottom: .7rem; }
.blog-card { display: block; padding: 1.6rem 0; border-bottom: 1px solid var(--border); text-decoration: none; }
.blog-card:first-of-type { border-top: 1px solid var(--border); }
.blog-card h2 { margin-bottom: .6rem; font-size: 1.8rem; }
.blog-card:hover h2 { color: var(--accent); }
.blog-card p { margin: 0; }
.work-section { margin-block: 1.5rem; padding: 1.8rem; border: 1px solid var(--border); background: var(--surface); border-radius: 5px; }
.work-section p:last-child { margin-bottom: 0; }
.work-title { font-size: 1.8rem; }
.work-subtitle { color: var(--muted); }
.reading-page { max-width: 780px; margin-inline: auto; }
.reading-page .work-section { background: none; border: 0; padding: 0; }
.reading-page p { line-height: 1.8; }
.tools-list { padding-left: 1.2rem; }
.tools-list li { padding-bottom: .5rem; }
label { font-size: .9rem; font-weight: 600; }
textarea,input { --pico-form-element-spacing-vertical: .7rem; font-size: .9rem; }
.error-message { color: var(--error); border-color: var(--error); }
#results:empty { display: none; }
.site-footer { display: flex; justify-content: space-between; align-items: center; gap: 2rem; border-top: 1px solid var(--border); padding-block: 1.6rem 2rem; font-size: .8rem; color: var(--muted); }
.site-footer p { margin: 0; }
.footer-links { display: flex; flex-wrap: wrap; gap: 1.3rem; }
.footer-links a { color: var(--muted); text-decoration: none; }
.footer-links a:hover { color: var(--accent); text-decoration: underline; }
pre { padding: 1.2rem; background: var(--code-bg); border: 1px solid var(--border); color: var(--text); font-size: .75rem; overflow-x: auto; }
pre code { background: none; color: inherit; padding: 0; }
blockquote { border-left-color: var(--accent); color: var(--text); }
@media (max-width: 900px) {
    .site-width { width: min(100% - 48px,1160px); }
    .nav-links { gap: 1.1rem; }
    .hero-section { gap: 2.4rem; }
    .hero-image { height: 285px; }
}
@media (max-width: 620px) {
    .site-width { width: calc(100% - 36px); }
    .site-nav { min-height: 110px; flex-wrap: wrap; justify-content: center; gap: .4rem; padding-block: .8rem; }
    .brand { width: 100%; text-align: center; font-size: 1.45rem; }
    .nav-links { gap: 1rem; justify-content: center; width: 100%; }
    .nav-item { font-size: .73rem; }
    .theme-toggle { font-size: .7rem; padding: .25rem .4rem; }
    .site-main { padding-block: 38px 44px; }
    .hero-section { grid-template-columns: 1fr; gap: 2rem; padding-bottom: 2.5rem; }
    .hero-title { font-size: 3.5rem; }
    .hero-subtitle { font-size: 1.1rem; }
    .hero-portrait { justify-self: start; width: 220px; }
    .hero-image { height: 250px; object-position: center; }
    .interest-grid { grid-template-columns: 1fr; gap: 1.8rem; }
    .section-heading { align-items: start; }
    .work-section { padding: 1.2rem; }
    .site-footer { align-items: flex-start; flex-direction: column; gap: 1rem; }
    .footer-links { gap: 1rem; }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
"""
