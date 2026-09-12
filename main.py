# main.py
from fasthtml.common import *
from pathlib import Path
from starlette.staticfiles import StaticFiles
from starlette.concurrency import run_in_threadpool
from air_quality import handle_aqi_request
from styles import BASE_STYLES, THEME_SCRIPT
from blogs import BLOG_POSTS
from projects import PROJECTS, project_card, project_section, frontline_page, otsc_page, otsc_walkthrough
css = Style(BASE_STYLES)
ASSETS = Path(__file__).resolve().parent / "assets"
app = FastHTML(
    hdrs=(
        Script("try { document.documentElement.dataset.theme = localStorage.getItem('theme') === 'dark' ? 'dark' : 'light'; } catch {}"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.1.1/css/pico.min.css"),
        css,
        Link(rel="icon", href="/public/avatar.jpg", type="image/jpeg"),
        Script(THEME_SCRIPT),
    ),
    htmx4=True,
    surreal=False,
    canonical=False,
    sess_cls=None,
    secret_key="sessions-disabled",
    htmlkw={"lang": "en", "data-theme": "light"},
)
# Keep the existing /public URLs, with assets bundled alongside the FastHTML app.
if ASSETS.is_dir():
    app.mount("/public", StaticFiles(directory=ASSETS), name="public")
rt = app.route


def nav_item(text, href, current_path):
    active = current_path == href or (href != "/" and current_path.startswith(href + "/"))
    return A(text, href=href, cls="nav-item active" if active else "nav-item", aria_current="page" if active else None)


def create_nav(current_path):
    return Header(
        Nav(
            Button(Span("◐", aria_hidden="true"), Span("Dark", data_theme_label=""),
                   id="theme-toggle", cls="theme-toggle", type="button", aria_label="Use dark theme", aria_pressed="false"),
            *(nav_item(label, url, current_path) for label, url in [("HOME", "/"), ("PROJECTS", "/projects"), ("ABOUT", "/about"), ("TOOLS", "/tools"), ("BLOG", "/blog")]),
            cls="site-nav site-width", aria_label="Main navigation",
        ), cls="site-header",
    )

def create_layout(current_path, *content, title=None, description=None):
    title = title or {"/about": "About", "/tools": "Tools", "/blog": "Writing"}.get(current_path)
    page_title = f"{title} | David Russell" if title else "David Russell — Software engineer"
    summary = description or "Software, systems, and applied AI. Projects and writing by David Russell."
    canonical = "https://davidrussell.dev" + current_path
    return (
        Title(page_title),
        Meta(name="description", content=summary),
        Link(rel="canonical", href=canonical),
        Meta(property="og:title", content=page_title),
        Meta(property="og:description", content=summary),
        Meta(property="og:type", content="article" if current_path.startswith("/blog/") else "website"),
        Meta(property="og:url", content=canonical),
        Meta(property="og:image", content="https://davidrussell.dev/public/avatar.jpg"),
        Meta(name="twitter:card", content="summary"),
        A("Skip to content", href="#main-content", cls="skip-link"),
        create_nav(current_path),
        Main(*content, id="main-content", cls="site-main site-width home-main" if current_path == "/" else "site-main site-width"),

    )


@rt("/")
def home(request):
    posts_sorted = []
    for slug, post in BLOG_POSTS.items():
        posts_sorted.append((slug, post))
        break
    first_slug, first_post = posts_sorted[0]
    blog_preview_title = first_post["title"]
    blog_preview_date = first_post["date"]
    blog_preview_snippet = first_post["snippet"]
    blog_preview_link = f"/blog/{first_slug}"

    content = Div(
        # Main hero section - center of screen
        Div(
            H1("DAVID RUSSELL", cls="hero-title"),
            P("Programmer", cls="hero-subtitle"),
            Img(src="/public/sun.png", alt="David Russell outdoors", cls="hero-image"),
            cls="hero-section"
        ),

        # Left sidebar with feature boxes
        Div(
            Div(
                H2("About Me", cls="feature-title"),
                P("In which I briefly describe the life and opinions of the eponymous David Russell.", cls="feature-description"),
                A("Learn More", href="/about", cls="feature-link"),
                cls="feature-box about-box",
            ),
            Div(
                H2("Blog", cls="feature-title"),
                A(
                    H3(blog_preview_title),
                    P(blog_preview_date),
                    P(blog_preview_snippet + "..."),
                    href=blog_preview_link,
                    cls="blog-preview-link",
                ),
                A("View All Posts", href="/blog", cls="feature-link"),
                cls="feature-box blog-box",
            ),
            Div(
                H2("Tools", cls="feature-title"),
                Ul(
                    Li(A("Air Quality Checker", href="/tools#air-quality-checker")),
                    Li(A("Hotdog vs Hamburger Classifier", href="/tools#hotdog-vs-hamburger-classifier")),
                    cls="tools-list"
                ),
                A("View All Tools", href="/tools", cls="feature-link"),
                cls="feature-box tools-box",
            ),
            cls="sidebar-left"
        ),

        # Social cards - bottom middle/right
        Div(
            A(
                Img(src="/public/avatar.jpg", alt="David Russell", cls="social-image"),
                Div(
                    H3("GitHub", cls="social-title"),
                    P("Check out my code repositories", cls="social-description"),
                ),
                href="https://github.com/russedavid",
                cls="social-card",
            ),
            A(
                Img(src="/public/withbike.png", alt="David with a bike", cls="social-image"),
                Div(
                    H3("LinkedIn", cls="social-title"),
                    P("Connect with me professionally", cls="social-description"),
                ),
                href="https://www.linkedin.com/in/davidrussellengineer/",
                cls="social-card",
            ),
            A(
                Img(src="/public/turbo.jpg", alt="Photo for David’s Twitter profile", cls="social-image"),
                Div(
                    H3("Twitter", cls="social-title"),
                    P("Follow my thoughts and updates", cls="social-description"),
                ),
                href="https://twitter.com/davidrusselldev",
                cls="social-card",
            ),
            A(
                Img(src="/public/hos.png", alt="High Order Software logo", cls="social-image logo-image"),
                Div(
                    H3("High Order Software", cls="social-title"),
                    P("Visit my consulting business homepage", cls="social-description"),
                ),
                href="https://hos.net",
                cls="social-card",
            ),
            cls="social-section"
        ),
        cls="homepage-container"
    )
    return create_layout(request.url.path, content, project_section())

@rt("/projects")
def projects_index(request):
    return create_layout(
        "/projects",
        Div(P("Selected work", cls="eyebrow"), H1("Software with a job to do."),
            P("Personal projects in applied AI: the product, the engineering decisions, and the evidence behind them."), cls="project-index-intro"),
        Div(*(project_card(project) for project in PROJECTS), cls="project-grid"),
        title="Projects",
    )


@rt("/projects/frontline")
def frontline(request):
    return create_layout(request.url.path, *frontline_page(), title="Frontline", description=PROJECTS[0]["description"])


@rt("/projects/otsc")
def otsc(request):
    try:
        step = int(request.query_params.get("step", "0"))
    except ValueError:
        step = 0
    step = step if 0 <= step < 3 else 0
    return create_layout(request.url.path, *otsc_page(step), title="Over The Shoulder Coder", description=PROJECTS[1]["description"])


@rt("/projects/otsc/walkthrough/{step:int}")
def sample_session(step: int):
    if step not in range(3):
        raise HTTPException(404)
    return otsc_walkthrough(step)


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


@rt("/robots.txt")
def robots():
    return Response("User-agent: *\nAllow: /\nDisallow: /check-aqi\nDisallow: /projects/otsc/walkthrough/\nSitemap: https://davidrussell.dev/sitemap.xml\n", media_type="text/plain")


@rt("/sitemap.xml")
def sitemap():
    from xml.sax.saxutils import escape
    paths = ["/", "/projects", "/projects/frontline", "/projects/otsc", "/about", "/tools", "/blog"]
    paths.extend(f"/blog/{slug}" for slug in BLOG_POSTS)
    urls = "".join(f"<url><loc>{escape('https://davidrussell.dev' + path)}</loc></url>" for path in paths)
    return Response('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>', media_type="application/xml")


if __name__ == "__main__":
    serve()
