from fasthtml.common import *
from styles import BASE_STYLES
from blogs import BLOG_POSTS

app, rt = fast_app(static_path="public")


def nav_item(text, href, current_path):
    active_class = "active" if href == current_path else ""
    return A(text, href=href, cls=f"nav-item {active_class}")


def create_nav(current_path):
    return Nav(
        Div(
            Button("🌙", cls="theme-toggle", id="theme-toggle"),
            nav_item("HOME", "/", current_path),
            nav_item("WORK", "/work", current_path),
            nav_item("AI", "/ai", current_path),
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
    return Container(
        Title(title),
        Meta(name="description", content="Full-stack Developer and AI Explorer"),
        Meta(property="og:title", content=title),
        Style(BASE_STYLES),
        create_nav(current_path),
        *content,
    )


@rt("/")
def home(request):
    content = Div(
        H1("DAVID RUSSELL"),
        P("Full-stack Developer // AI Explorer // Digital Craftsman", cls="subtitle"),
        Img(src="/sun.png", alt="David with a bike", cls="profile-image"),
        Div(
            A(
                Img(src="./avatar.jpg", cls="social-image"),
                Div(
                    H3("GitHub", cls="social-title"),
                    P("Check out my code repositories", cls="social-description"),
                ),
                href="https://github.com/russedavid",
                cls="social-card",
            ),
            A(
                Img(src="/withbike.png", cls="social-image"),
                Div(
                    H3("LinkedIn", cls="social-title"),
                    P("Connect with me professionally", cls="social-description"),
                ),
                href="https://www.linkedin.com/in/davidrussellengineer/",
                cls="social-card",
            ),
            A(
                Img(src="/turbo.jpg", cls="social-image"),
                Div(
                    H3("Twitter", cls="social-title"),
                    P("Follow my thoughts and updates", cls="social-description"),
                ),
                href="https://twitter.com/davidtherusse",
                cls="social-card",
            ),
        ),
    )
    return create_layout(request.url.path, content)


@rt("/work")
def work(request):
    content = Div(
        H1("MY WORK"),
        Div(
            H2("Corbalt", cls="work-title"),
            P("Software Developer", cls="work-subtitle"),
            P(
                "At ",
                A("Corbalt", href="https://www.corbalt.com/"),
                " I help my team and the government make great decisions about how to build and maintain software that scales.",
            ),
            cls="work-section",
        ),
        Div(
            H2("ATX LED", cls="work-title"),
            P("Software Developer", cls="work-subtitle"),
            P(
                """I started working with """,
                A("ATX LED", href="https://atxledinc.com"),
                """ in 2023. Since then, I've shipped hundreds of new features, integrations and improvements to the ATX LED home automation hub using JavaScript, React, Python and more.""",
            ),
            cls="work-section",
        ),
        Div(
            H2("Amazon Web Services", cls="work-title"),
            P("Software Developer", cls="work-subtitle"),
            Ul(
                Li("I started at AWS as an intern in 2020."),
                Li(
                    "I returned as a full-time software developer in 2021, in the World Wide Revenue Operations org."
                ),
                Li(
                    "I helped build the SUDS (Sales Unified Data Service), a graphql based server meant to provide a single point of access to the entirety of the sales and marketing data available at AWS."
                ),
                Li(
                    "I built a developer experience for on-boarding data sources to SUDS that was intuitive and pain free."
                ),
                Li(
                    "SUDS received a mandate to on-board all first-party software teams in WWRO"
                ),
            ),
            cls="work-section",
        ),
    )
    return create_layout(request.url.path, content)


@rt("/ai")
def ai(request):
    content = Div(
        H1("AI PROJECTS"),
        Div(
            H2("Hotdog vs Hamburger Classifier", cls="work-title"),
            P("A fine-tuned ResNet model for food classification", cls="work-subtitle"),
            Iframe(
                src="https://davidrussell-hamburger-or-hotdog.hf.space",
                style="width:100%; height:600px; border:0; border-radius: 8px; margin:2rem 0;",
            ),
            cls="work-section",
        ),
    )
    return create_layout(request.url.path, content)





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


@rt("/{fname:path}.{ext:static}")
def static_files(request):
    fname = request.path_params["fname"]
    ext = request.path_params["ext"]
    return FileResponse(f"public/{fname}.{ext}")


serve()
