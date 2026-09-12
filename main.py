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
    hdrs=(Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.1.1/css/pico.min.css"), css),
    htmx4=True,
    surreal=False,
    sess_cls=None,
    secret_key="sessions-disabled",
    htmlkw={"lang": "en"},
)
app.mount("/public", StaticFiles(directory=PUBLIC), name="public")
rt = app.route


def nav_item(text, href, current_path):
    active_class = "active" if href == current_path else ""
    return A(text, href=href, cls=f"nav-item {active_class}")


def create_nav(current_path):
    return Nav(
        Div(
            Button("🌙", cls="theme-toggle", id="theme-toggle"),
            nav_item("HOME", "/", current_path),
            nav_item("ABOUT", "/about", current_path),
            nav_item("TOOLS", "/tools", current_path),
            nav_item("BLOG", "/blog", current_path),
            cls="nav-container",
        ),
        Script(
            """
            const toggle = document.getElementById('theme-toggle');
            const root = document.documentElement;
            
            const savedTheme = localStorage.getItem('theme') || 'dark';
            if (savedTheme === 'light') {
                root.classList.add('light-theme');
                toggle.textContent = '☀️';
            }
            
            toggle.addEventListener('click', () => {
                root.classList.toggle('light-theme');
                toggle.textContent = root.classList.contains('light-theme') ? '☀️' : '🌙';
                localStorage.setItem('theme', root.classList.contains('light-theme') ? 'light' : 'dark');
            });
        """
        ),
    )


def create_layout(current_path, *content):
    title = "David Russell - Developer"
    return Title(title), Main(
        create_nav(current_path),
        *content,
        cls="container",
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
            Img(src="public/sun.png", alt="David with a bike", cls="hero-image"),
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
                    A(Li("Air Quality Checker"), href="/tools#air-quality-checker"),
                    A(Li("Hotdog vs Hamburger Classifier"), href="/tools#hotdog-vs-hamburger-classifier"),
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
                Img(src="public/avatar.jpg", cls="social-image"),
                Div(
                    H3("GitHub", cls="social-title"),
                    P("Check out my code repositories", cls="social-description"),
                ),
                href="https://github.com/russedavid",
                cls="social-card",
            ),
            A(
                Img(src="public/withbike.png", cls="social-image"),
                Div(
                    H3("LinkedIn", cls="social-title"),
                    P("Connect with me professionally", cls="social-description"),
                ),
                href="https://www.linkedin.com/in/davidrussellengineer/",
                cls="social-card",
            ),
            A(
                Img(src="public/turbo.jpg", cls="social-image"),
                Div(
                    H3("Twitter", cls="social-title"),
                    P("Follow my thoughts and updates", cls="social-description"),
                ),
                href="https://twitter.com/davidrusselldev",
                cls="social-card",
            ),
            A(
                Img(src="public/hos.png", cls="social-image"),
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
    return create_layout(request.url.path, content)


@rt("/about")
def about(request):
    content = Div(
        H1("ABOUT ME"),
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
        H1("TOOLS"),
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
    return create_layout(request.url.path, content)


@rt("/blog")
def blog(request):
    content = Div(
        H1("BLOG"),
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
