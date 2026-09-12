# main.py
from fasthtml.common import *
from pathlib import Path
from starlette.staticfiles import StaticFiles
from starlette.concurrency import run_in_threadpool
from air_quality import handle_aqi_request
from styles import BASE_STYLES
from blogs import BLOG_POSTS
css = Style(BASE_STYLES)
PUBLIC = Path(__file__).resolve().parent / "public"
app = FastHTML(
    hdrs=(
        Script("try { document.documentElement.dataset.theme = localStorage.getItem('theme') === 'dark' ? 'dark' : 'light'; } catch {}"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.1.1/css/pico.min.css"),
        css,
        Script(src="/public/site.js", defer=True),
    ),
    htmx4=True,
    surreal=False,
    sess_cls=None,
    secret_key="sessions-disabled",
    htmlkw={"lang": "en", "data-theme": "light"},
)
app.mount("/public", StaticFiles(directory=PUBLIC), name="public")
rt = app.route


def nav_item(text, href, current_path):
    active = current_path == href or (href != "/" and current_path.startswith(href + "/"))
    return A(text, href=href, cls="nav-item active" if active else "nav-item", aria_current="page" if active else None)


def create_nav(current_path):
    return Header(
        Nav(
            A("dr.", href="/", cls="brand", aria_label="David Russell home"),
            Div(
                *(nav_item(label, url, current_path) for label, url in [("Home", "/"), ("About", "/about"), ("Tools", "/tools"), ("Blog", "/blog")]),
                Button(Span("◐", aria_hidden="true"), Span("Dark", data_theme_label=""),
                       id="theme-toggle", cls="theme-toggle", type="button", aria_label="Use dark theme", aria_pressed="false"),
                cls="nav-links",
            ),
            cls="site-nav site-width", aria_label="Main navigation",
        ), cls="site-header",
    )


def create_layout(current_path, *content, title=None, description=None):
    page_title = f"{title} | David Russell" if title else "David Russell — Software engineer"
    return (
        Title(page_title),
        Meta(name="description", content=description or "Software, systems, and applied AI. Projects and writing by David Russell."),
        A("Skip to content", href="#main-content", cls="skip-link"),
        create_nav(current_path),
        Main(*content, id="main-content", cls="site-main site-width"),
        Footer(
            P("David Russell"),
            Div(
                A("GitHub", href="https://github.com/russedavid"),
                A("LinkedIn", href="https://www.linkedin.com/in/davidrussellengineer/"),
                A("Twitter", href="https://twitter.com/davidrusselldev"),
                A("High Order Software", href="https://hos.net"),
                cls="footer-links",
            ), cls="site-footer site-width",
        ),
    )


@rt("/")
def home(request):
    slug, latest = next(iter(BLOG_POSTS.items()))
    return create_layout(
        "/",
        Section(
            Div(
                P("Software / Systems / Applied AI", cls="eyebrow"),
                H1("David Russell", cls="hero-title"),
                P("I build software, design systems, and make tools that help people do both.", cls="hero-subtitle"),
                Div(A("More about me", href="/about", cls="button-link"),
                    A("Find me on GitHub ↗", href="https://github.com/russedavid", cls="text-link"), cls="actions"),
            ),
            Figure(Img(src="/public/sun.png", alt="David Russell outdoors", cls="hero-image", width=315, height=335), cls="hero-portrait"),
            cls="hero-section",
        ),
        Section(
            P("A few other interests", cls="eyebrow"),
            Div(
                Div(P("From the blog", cls="blog-date"), H3(A(latest["title"], href=f"/blog/{slug}")),
                    P(latest["snippet"]), A("All writing →", href="/blog", cls="text-link")),
                Div(P("Small tools & experiments", cls="blog-date"), H3("Useful. Occasionally curious."),
                    Ul(Li(A("Air Quality Checker", href="/tools#air-quality-checker")),
                       Li(A("Hotdog vs Hamburger Classifier", href="/tools#hotdog-vs-hamburger-classifier")), cls="tools-list"),
                    A("All tools →", href="/tools", cls="text-link")),
                cls="interest-grid",
            ), cls="interests",
        ),
    )


@rt("/about")
def about(request):
    content = Div(
        P("Beyond the code", cls="eyebrow"),
        H1("About me"),
        Div(
            P("In addition to writing code, designing systems, and building tools that make the aforementioned easier, I:"),
            Ul(
                Li("Am a full-time enjoyer of collaborative storytelling modalities."),
                Li("Explore new technologies and apply them to real-world problems."),
                Li("Read psychological literary fiction and watch deep, meaning-filled films."),
            ),
            cls="work-section",
        ),
    )
    return create_layout(request.url.path, content)


@rt("/tools")
def tools(request):
    content = Div(
        P("Small tools & experiments", cls="eyebrow"),
        H1("Tools"),
        Div(
            H2("Air Quality Checker", cls="work-title", id="air-quality-checker"),
            Form(
                Label("Coordinates (latitude, longitude)", fr="coordinates"),
                Textarea(
                    id="coordinates", name="coordinates", required=True,
                    placeholder="Enter coordinates (lat,lon) - one per line\nExample:\n30.5002452018897,-97.7907459171229",
                    rows=10,
                    cls="w-full p-2",
                ),
                Label("Google Air Quality API key", fr="api_key"),
                Input(
                    id="api_key", name="api_key", required=True, autocomplete="off",
                    type="password",
                    placeholder="Google Maps API Key",
                    cls="w-full p-2",
                ),
                Button("Check Air Quality", type="submit", cls="mt-4"),
                method="post", action="/check-aqi",
                hx_post="/check-aqi",
                hx_disabled_elt="find button",
                hx_target="#results",
            ),
            Div(id="results", aria_live="polite"),
            cls="work-section",
        ),
        Div(
            H2("Hotdog vs Hamburger Classifier", cls="work-title", id="hotdog-vs-hamburger-classifier"),
            P("A fine-tuned ResNet model for food classification", cls="work-subtitle"),
            Iframe(
                src="https://davidrussell-hamburger-or-hotdog.hf.space",
                title="Hotdog versus hamburger classifier", loading="lazy",
                style="width:100%; height:600px; border:0; border-radius: 8px; margin:2rem 0;",
            ),
            cls="work-section",
        ),
    )
    return create_layout(request.url.path, content)


def aqi_result(result):
    heading = H3("Location: " + ", ".join(map(str, result["coordinates"])))
    if "error" in result:
        return Div(heading, P(result["error"], role="alert"), cls="work-section error-message")
    data = result["data"]
    if data["average_aqi"] is None:
        return Div(heading, P("No air-quality readings were returned for this location."), cls="work-section")
    return Div(
        heading,
        P(f"Average AQI: {data['average_aqi']:.2f}"),
        P("Most common dominant pollutant: " + (data["dominant_pollutant"][0][0] if data["dominant_pollutant"] else "Not reported")),
        H4("Average pollutant concentrations"),
        Ul(*(Li(f"{name}: {value:.2f}") for name, value in data["pollutant_averages"].items()))
        if data["pollutant_averages"] else P("No concentrations were reported."),
        cls="work-section",
    )


@rt("/check-aqi")
async def post(request):
    form = await request.form()
    api_key = str(form.get("api_key", "")).strip()
    coordinates = str(form.get("coordinates", "")).strip()
    if not api_key or not coordinates:
        output = Div(P("Enter an API key and at least one latitude,longitude pair.", role="alert"), cls="error-message")
    else:
        results = await run_in_threadpool(handle_aqi_request, api_key, coordinates)
        output = Div(*(aqi_result(result) for result in results))
    if request.headers.get("hx-request"):
        return output
    return create_layout("/tools", H1("Air quality results"), output, A("Back to tools", href="/tools"))


@rt("/blog/{slug}")
def blog_post(request):
    slug = request.path_params["slug"]
    post = BLOG_POSTS.get(slug)
    if not post:
        return RedirectResponse("/blog")

    content = Div(
        H1(post["title"]),
        P(post["date"], cls="blog-date"),
        Div(post["content"], cls="work-section"),
    )
    return create_layout(request.url.path, Div(content, cls="reading-page"), title=post["title"], description=post["snippet"])


@rt("/blog")
def blog(request):
    content = Div(
        P("Notes on software and other things", cls="eyebrow"),
        H1("Writing"),
        *[
            A(
                H2(post["title"], cls="blog-title"),
                P(post["date"], cls="blog-date"),
                href=f"/blog/{slug}",
                cls="blog-card",
            )
            for slug, post in BLOG_POSTS.items()
        ],
    )
    return create_layout(request.url.path, content)


if __name__ == "__main__":
    serve()
