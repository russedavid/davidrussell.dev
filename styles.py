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

BASE_STYLES += """
.project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 1.6rem; }
.project-card { padding: 0; margin: 0; border: 1px solid var(--border); border-radius: 6px; background: var(--surface); box-shadow: none; overflow: hidden; }
.project-copy { padding: 1.6rem; }
.project-copy h3 { font-size: 1.9rem; margin-bottom: .6rem; }
.project-copy h3 a { text-decoration: none; color: var(--text); }
.project-copy h3 a:hover { color: var(--accent); }
.project-status { font-size: .7rem; color: var(--accent); font-weight: 600; margin-bottom: .7rem; }
.project-tagline { color: var(--text); font-size: 1.03rem; margin-bottom: .65rem; }
.project-description { font-size: .93rem; color: var(--muted); }
.project-stack { font-size: .7rem; color: var(--muted); margin-top: 1.2rem; }
.project-preview { padding: 1.3rem; background: var(--highlight); min-height: 282px; border-bottom: 1px solid var(--border); }
.preview-bar { display: flex; justify-content: space-between; gap: 1rem; align-items: center; border-bottom: 1px solid var(--strong-border); padding-bottom: .6rem; margin-bottom: .7rem; }
.preview-brand { font-size: .65rem; font-weight: 600; letter-spacing: .15em; }
.preview-label { font-size: .65rem; color: var(--muted); }
.report-paper { background: var(--surface); padding: .9rem 1.1rem; border: 1px solid var(--border); }
.report-heading { font-family: 'Source Serif', Georgia, serif; font-size: 1.1rem; margin: 0 0 .7rem; }
.report-line { display: grid; grid-template-columns: 85px 1fr; gap: .7rem; margin-block: .6rem; align-items: baseline; }
.report-line p { font-size: .78rem; margin: 0; }
.state-label { color: var(--success); font-size: .55rem; letter-spacing: .07em; font-weight: 600; }
.preview-footnote { margin: .9rem 0 0; font-size: .6rem; color: var(--muted); }
.back-link { font-size: .8rem; text-decoration: none; }
.project-hero { padding-block: 2.5rem 3rem; max-width: 900px; }
.project-hero h1 { font-size: clamp(2.5rem, 5.4vw, 4rem); }
.project-lede { font-size: 1.2rem; line-height: 1.6; color: var(--muted); max-width: 780px; }
.example-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; padding-block: 2rem 3rem; border-top: 1px solid var(--border); }
.example-grid .project-preview { border: 1px solid var(--border); border-radius: 5px; }
.example-grid blockquote { padding: .2rem 0 .2rem 1.3rem; margin-block: 1.5rem; font-family: 'Source Serif', Georgia, serif; font-size: 1.25rem; }
.case-section { padding-block: 2.7rem; border-top: 1px solid var(--border); }
.case-section > p:not(.eyebrow) { max-width: 800px; }
.case-section h2 { margin-bottom: 1.5rem; }
.workflow-list { counter-reset: steps; padding: 0; list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 1.4rem 3rem; }
.workflow-list li { position: relative; counter-increment: steps; padding-left: 2.5rem; font-size: .95rem; color: var(--muted); }
.workflow-list li::before { content: '0' counter(steps); position: absolute; left: 0; top: 0; font-size: .8rem; color: var(--accent); }
.workflow-list strong { display: block; color: var(--text); }
.decision-row { display: grid; grid-template-columns: 1fr 2fr; gap: 2rem; border-bottom: 1px solid var(--border); padding-block: 1.4rem; }
.decision-row:last-child { border-bottom: 0; }
.decision-row h3 { margin: 0; font-size: 1.4rem; }
.decision-row p { margin: 0; color: var(--muted); }
.muted { color: var(--muted); }
.small-note { font-size: .8rem; color: var(--muted); }
.project-outro { background: var(--highlight); padding: 2.5rem; border-radius: 5px; margin-top: 1rem; }
.project-outro h2 { max-width: 750px; }
.project-index-intro { max-width: 750px; margin-bottom: 2.8rem; }
.project-index-intro p:not(.eyebrow) { color: var(--muted); font-size: 1.15rem; }
@media (max-width: 700px) {
    .project-grid,.example-grid,.workflow-list { grid-template-columns: 1fr; }
    .project-copy { padding: 1.3rem; }
    .project-hero { padding-block: 2rem; }
    .example-grid { gap: 1.4rem; }
    .decision-row { grid-template-columns: 1fr; gap: .7rem; }
    .project-outro { padding: 1.5rem; }
    .project-preview { padding: 1rem; }
    .nav-links { gap: .8rem; }
    .section-heading h2 { font-size: 2rem; }
}
"""

BASE_STYLES += """
.assistant-paper { padding: .9rem 1.1rem; border: 1px solid var(--border); background: var(--surface); }
.mini-tabs { display: flex; gap: .9rem; border-bottom: 1px solid var(--border); padding-bottom: .5rem; }
.mini-tab { font-size: .65rem; color: var(--muted); }
.mini-tab.selected { color: var(--accent); font-weight: 600; }
.task-brief { font-size: .7rem; margin: .7rem 0; }
.assistant-paper pre { margin: 0; padding: .6rem; font-size: .63rem; border: 0; line-height: 1.7; }
.walkthrough { margin-block: 1.7rem 1rem; border: 1px solid var(--border); border-radius: 5px; overflow: hidden; }
.walkthrough-controls { display: flex; gap: .5rem; flex-wrap: wrap; padding: 1rem; border-bottom: 1px solid var(--border); background: var(--highlight); }
.walkthrough-step { padding: .5rem .8rem; font-size: .78rem; color: var(--muted); text-decoration: none; border: 1px solid transparent; border-radius: 4px; }
.walkthrough-step.selected { background: var(--surface); color: var(--text); border-color: var(--strong-border); }
.walkthrough-step:hover { text-decoration: underline; }
.walkthrough-body { display: grid; grid-template-columns: 1fr 1.2fr; background: var(--surface); }
.sample-context,.sample-artifact { min-width: 0; padding: 1.6rem; }
.sample-context { border-right: 1px solid var(--border); }
.sample-context h3 { font-size: 1.5rem; margin-block: 1.4rem .8rem; }
.sample-context p { color: var(--muted); font-size: .9rem; }
.sample-input { white-space: pre-wrap; overflow-wrap: anywhere; border: 0; padding: 0; background: transparent; font-family: 'Source Sans',sans-serif; font-size: 1rem; }
.sample-input code { font: inherit; }
.sample-code { margin-bottom: 1rem; min-height: 280px; font-size: .68rem; line-height: 1.8; }
.context-flow { display: grid; grid-template-columns: repeat(4,1fr); gap: 1.4rem; margin-block: 2rem; }
.context-flow > div { border-top: 2px solid var(--strong-border); padding-top: .8rem; }
.flow-number { display: block; font-size: .7rem; color: var(--accent); margin-bottom: .6rem; }
.context-flow strong { font-size: .95rem; }
.context-flow p { font-size: .83rem; color: var(--muted); margin-top: .6rem; }
@media (max-width: 800px) {
    .walkthrough-body { grid-template-columns: 1fr; }
    .sample-context { border-right: 0; border-bottom: 1px solid var(--border); }
    .context-flow { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 450px) {
    .sample-context,.sample-artifact { padding: 1rem; }
    .walkthrough-controls { gap: .2rem; }
    .walkthrough-step { padding: .5rem; }
    .project-preview { min-height: 0; }
    .section-heading h2 { font-size: 1.7rem; }
}
"""

BASE_STYLES += """
.career-paper blockquote { font: 1rem/1.45 'Source Serif', Georgia, serif; margin: .8rem 0; padding: .3rem 0 .3rem .8rem; }
.career-example-claim { font: 1.1rem/1.5 'Source Serif', Georgia, serif; color: var(--text); }
.career-paper .career-example-claim { font-size: .88rem; }
.career-artifact { padding: 1.5rem; }
.career-artifact .career-example-claim { padding-block: 1.1rem; }
.model-paper { background: var(--surface); border: 1px solid var(--border); padding: 1rem; text-align: center; }
.model-base-label { margin: 0; color: var(--muted); font-size: .7rem; }
.model-size { display: block; font: 3.6rem/1.2 'Source Serif', Georgia, serif; color: var(--text); }
.model-base-caption { margin: .2rem 0 1rem; font-size: .7rem; }
.adapter-labels { display: flex; flex-wrap: wrap; justify-content: center; gap: .4rem; }
.adapter-labels span { padding: .25rem .5rem; border: 1px solid var(--strong-border); border-radius: 3px; font-size: .6rem; }
.training-example pre { font: .95rem/1.6 'Source Serif', Georgia, serif; white-space: pre-wrap; overflow-wrap: anywhere; padding: 0; margin: 0; background: transparent; border: 0; }
.training-label { font: 600 .7rem/1.5 'Source Sans', sans-serif; color: var(--accent); margin-bottom: .6rem; }
.training-context { padding-bottom: 1.3rem; color: var(--muted); }
.training-target { padding: 1rem; border-left: 3px solid var(--strong-border); background: var(--highlight); }
.training-example > .small-note { margin-top: 1rem; }
.historical-claim { text-decoration: line-through; color: var(--muted); }
.setup-code { padding: 1.5rem; background: var(--code-bg); border: 1px solid var(--border); white-space: pre-wrap; overflow-wrap: anywhere; }
.setup-code code { white-space: pre-wrap; overflow-wrap: anywhere; }

/* Align the previews and reading links in the two-column project grid. */
.project-card { display: flex; flex-direction: column; }
.project-card > .project-preview { min-height: 338px; }
.project-copy { display: flex; flex-direction: column; flex: 1; }
.project-copy > .text-link { margin-top: auto; align-self: flex-start; }
.project-copy .project-stack { margin-bottom: 1.3rem; }
@media (max-width: 700px) { .project-card > .project-preview { min-height: 0; } }
"""


THEME_SCRIPT = """
(() => {
  const root = document.documentElement;
  const update = () => {
    const toggle = document.getElementById('theme-toggle');
    if (!toggle) return;
    const dark = root.dataset.theme === 'dark';
    toggle.setAttribute('aria-label', dark ? 'Use light theme' : 'Use dark theme');
    toggle.setAttribute('aria-pressed', String(dark));
    toggle.querySelector('[data-theme-label]').textContent = dark ? 'Light' : 'Dark';
  };
  document.addEventListener('click', event => {
    if (!event.target.closest('#theme-toggle')) return;
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch {}
    update();
  });
  document.addEventListener('DOMContentLoaded', update);
})();
"""

BASE_STYLES += """
/* Preserve the original homepage composition and its prominent picture cards. */
.site-header { position: sticky; top: 0; z-index: 1000; background: var(--background); }
.site-nav { min-height: 66px; gap: 1rem; justify-content: space-between; }
.site-nav .nav-item { font-size: .85rem; }
.site-nav .theme-toggle { flex-shrink: 0; }
.home-main { padding-top: 34px; }
.homepage-container { display: grid; grid-template-areas: 'sidebar hero social'; grid-template-columns: minmax(0,1fr) minmax(0,1fr) minmax(0,1fr); gap: 20px; align-items: start; margin-bottom: 3rem; }
.homepage-container .hero-section { grid-area: hero; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0; padding: 0; }
.homepage-container .hero-title { font: 600 clamp(1.4rem,2.4vw,2.3rem)/1.1 'Source Sans',Arial,sans-serif; letter-spacing: -.04em; margin: 0; white-space: nowrap; }
.homepage-container .hero-subtitle { font-style: italic; font-size: 1.15rem; color: var(--text); margin: .65rem 0 1rem; }
.homepage-container .hero-image { width: 200px; max-width: 100%; height: auto; object-fit: contain; border-radius: 0; }
.sidebar-left { grid-area: sidebar; display: flex; flex-direction: column; gap: 0; }
.feature-box { padding: 16px; border: 1px solid var(--border); background: var(--surface); }
.feature-box + .feature-box { border-top: 0; }
.feature-title { font: 600 1.2rem/1.3 'Source Sans',sans-serif; margin: 0 0 .85rem; }
.feature-description { font-size: .95rem; line-height: 1.5; margin-bottom: 1rem; }
.feature-link { display: inline-block; padding: .45rem .8rem; border: 1px solid var(--strong-border); text-decoration: none; font-size: .85rem; font-weight: 600; }
.feature-link:hover { background: var(--highlight); }
.blog-preview-link { display: block; text-decoration: none; }
.blog-preview-link h3 { font: 600 1.2rem/1.3 'Source Sans',sans-serif; color: var(--accent); margin: .7rem 0; }
.blog-preview-link p { font-size: .9rem; color: var(--muted); }
.blog-preview-link:hover h3 { text-decoration: underline; }
.feature-box .tools-list { font-size: .9rem; padding-left: 1.1rem; }
.social-section { grid-area: social; display: flex; flex-direction: column; gap: 15px; }
.social-card { display: flex; gap: 15px; align-items: center; padding: 15px; border: 1px solid var(--border); text-decoration: none; color: var(--text); background: var(--surface); }
.social-card:hover { border-color: var(--accent); background: var(--highlight); color: var(--text); }
.social-card > div { min-width: 0; }
.social-image { width: 50px; height: 50px; flex: 0 0 50px; object-fit: cover; border-radius: 0; }
.logo-image { object-fit: contain; }
.social-title { font: 600 1.05rem/1.3 'Source Sans',sans-serif; margin: 0 0 .3rem; }
.social-description { font-size: .83rem; line-height: 1.4; margin: 0; }
@media (max-width: 850px) {
    .homepage-container { grid-template-areas: 'hero hero' 'sidebar social'; grid-template-columns: minmax(0,1fr) minmax(0,1fr); }
    .homepage-container .hero-section { margin-bottom: 1rem; }
    .homepage-container .hero-title { font-size: 2.4rem; }
}
@media (max-width: 620px) {
    .site-nav { min-height: 72px; flex-wrap: nowrap; gap: .5rem; padding-block: .6rem; }
    .site-nav .nav-item { font-size: .63rem; }
    .site-nav .theme-toggle { padding: .2rem .35rem; font-size: .65rem; }
    .homepage-container { grid-template-areas: 'hero' 'social' 'sidebar'; grid-template-columns: 1fr; gap: 1.6rem; }
    .homepage-container .hero-title { font-size: 2.1rem; }
}
"""
