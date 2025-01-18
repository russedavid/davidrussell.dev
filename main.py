from fasthtml.common import *
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import requests
from styles import BASE_STYLES
from blogs import BLOG_POSTS

app, rt = fast_app()


def calculate_aqi_stats(hours_info):
    """Process AQI data and return stats"""
    total_aqi = 0
    count = 0
    dominant_pollutants = Counter()
    pollutant_details = defaultdict(list)
    local_offset = timedelta(hours=-5)

    for hour in hours_info:
        if not hour.get("indexes"):
            continue

        utc_time = datetime.strptime(hour["dateTime"], "%Y-%m-%dT%H:%M:%SZ")
        local_time = utc_time + local_offset

        if 0 <= local_time.hour < 25:
            for index in hour.get("indexes"):
                aqi = index.get("aqi", 0)
                total_aqi += aqi
                count += 1

                if dominant_pollutant := index.get("dominantPollutant"):
                    dominant_pollutants[dominant_pollutant] += 1

            # Process pollutant concentrations
            for pollutant in hour.get("pollutants", []):
                if "concentration" in pollutant and (code := pollutant.get("code")):
                    pollutant_details[code].append(pollutant["concentration"]["value"])

    # Calculate averages
    average_aqi = total_aqi / count if count > 0 else 0
    pollutant_averages = {
        code: sum(values) / len(values) for code, values in pollutant_details.items()
    }

    return {
        "average_aqi": average_aqi,
        "dominant_pollutant": dominant_pollutants.most_common(1),
        "pollutant_averages": pollutant_averages,
    }


def fetch_aqi_data(api_key, lat, lon):
    """Fetch all pages of AQI data"""
    url = f"https://airquality.googleapis.com/v1/history:lookup?key={api_key}"
    data = {
        "hours": 720,
        "location": {"latitude": lat, "longitude": lon},
        "pageSize": 100,
        "extraComputations": ["POLLUTANT_CONCENTRATION"],
    }

    all_hours_info = []
    next_page_token = None

    while True:
        if next_page_token:
            data["pageToken"] = next_page_token

        try:
            response = requests.post(url, json=data).json()
            if "error" in response:
                raise ValueError(
                    f"API Error: {response['error'].get('message', 'Unknown error')}"
                )

            if hours_info := response.get("hoursInfo", []):
                all_hours_info.extend(hours_info)

            if not (next_page_token := response.get("nextPageToken")):
                break

        except requests.RequestException as e:
            raise ValueError(f"Request failed: {str(e)}")

    return calculate_aqi_stats(all_hours_info)


def handle_aqi_request(api_key, coordinates_text):
    """Process multiple coordinates and return results"""
    results = []

    for line in coordinates_text.strip().split("\n"):
        if not line.strip():
            continue

        try:
            lat, lon = map(float, line.strip().split(","))
            result = fetch_aqi_data(api_key, lat, lon)
            results.append({"coordinates": (lat, lon), "data": result})
        except (ValueError, IndexError) as e:
            results.append({"coordinates": (line.strip(),), "error": str(e)})

    return results


def nav_item(text, href, current_path):
    active_class = "active" if href == current_path else ""
    return A(text, href=href, cls=f"nav-item {active_class}")


def create_nav(current_path):
    return Nav(
        Div(
            Button("🌙", cls="theme-toggle", id="theme-toggle"),
            nav_item("HOME", "/", current_path),
            nav_item("WORK", "/work", current_path),
            nav_item("APPS", "/apps", current_path),
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
        Img(src="public/sun.png", alt="David with a bike", cls="profile-image"),
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


@rt("/apps")
def ai(request):
    content = Div(
        H1("APPS"),
        Div(
            H2("Air Quality Checker", cls="work-title"),
            Form(
                Textarea(
                    id="coordinates",
                    placeholder="Enter coordinates (lat,lon) - one per line\nExample:\n30.5002452018897,-97.7907459171229",
                    rows=10,
                    cls="w-full p-2",
                ),
                Input(
                    id="api_key",
                    type="password",
                    placeholder="Google Maps API Key",
                    cls="w-full p-2",
                ),
                Button("Check Air Quality", type="submit", cls="mt-4"),
                hx_post="/check-aqi",
                hx_target="#results",
            ),
            Div(id="results", cls="work-section"),
            cls="work-section",
        ),
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


@rt("/check-aqi")
async def post(request):
    form = await request.form()
    api_key = form.get("api_key")
    coordinates = form.get("coordinates")

    try:
        results = handle_aqi_request(api_key, coordinates)
        return Div(
            *[
                Div(
                    H3(
                        f"Location: {result['coordinates'][0]}, {result['coordinates'][1]}"
                    ),
                    P(f"Average AQI: {result['data']['average_aqi']:.2f}"),
                    *(
                        []
                        if "error" in result
                        else [
                            P(
                                f"Most Common Pollutant: {result['data']['dominant_pollutant'][0][0]} "
                                f"(Count: {result['data']['dominant_pollutant'][0][1]})"
                            ),
                            H4("Average Pollutant Concentrations:"),
                            Ul(
                                *[
                                    Li(f"{pollutant}: {avg:.2f}")
                                    for pollutant, avg in result["data"][
                                        "pollutant_averages"
                                    ].items()
                                ]
                            ),
                        ]
                    ),
                    cls="mt-4 p-4 border rounded work-section",
                )
                for result in results
            ]
        )
    except Exception as e:
        return Div(
            P(f"Error: {str(e)}", cls="text-red-600"),
            cls="mt-4 p-4 border border-red-600 rounded",
        )


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
