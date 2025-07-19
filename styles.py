# styles.py
BASE_STYLES = """
:root {
    --background: #ffffff;
    --text: #000000;
    --highlight: #f0f0f0;
    --border: #dddddd;
}

body {
    background: var(--background);
    color: var(--text);
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    min-height: 100vh;
}

html {
    scroll-padding-top: 75px;
}

a {
    color: var(--link);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.container {
    width: 100%;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

/* Navigation at top */
.nav-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3px 30px;
    background: var(--background);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(10px);
}

.nav-item {
    margin-left: 20px;
    font-weight: 500;
}

.active {
    font-weight: bold;
}

.theme-toggle {
    background: none;
    border: none;
    font-size: 1.5em;
    cursor: pointer;
}

/* Homepage landscape layout */
.homepage-container {
    display: grid;
    grid-template-areas: 
        "sidebar hero social";
    grid-template-columns: 350px 1fr 350px;
    grid-template-rows: 1fr;
    min-height: 100vh;
    padding-top: 3px;
    gap: 15px;
    padding-left: 30px;
    padding-right: 30px;
    box-sizing: border-box;
}

/* Hero section - center */
.hero-section {
    grid-area: hero;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    text-align: center;
    padding: 0;
}

.hero-title {
    font-size: 2.5rem;
    margin: 0;
    font-weight: bold;
    letter-spacing: -2px;
}

.hero-subtitle {
    font-size: 1.2rem;
    font-style: italic;
    margin: 10px 0 15px 0;
    color: var(--text);
}

.hero-image {
    max-width: 200px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

/* Left sidebar with feature boxes */
.sidebar-left {
    grid-area: sidebar;
    display: flex;
    flex-direction: column;
    gap: 0;
    padding: 0;
}

.feature-box {
    padding: 12px;
    border: 1px solid var(--border);
    background: transparent;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.feature-box:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.feature-title {
    margin: 0 0 15px 0;
    font-size: 1.3rem;
    font-weight: 600;
}

.feature-description {
    margin: 0 0 15px 0;
    color: var(--text);
    line-height: 1.5;
}

.feature-link {
    display: inline-block;
    margin-top: 10px;
    padding: 8px 16px;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--text);
    font-weight: 500;
    transition: opacity 0.2s ease;
}

.feature-link:hover {
    opacity: 0.8;
    text-decoration: none;
}

.tools-list {
    margin: 10px 0;
    padding-left: 20px;
}

.tools-list li {
    margin: 8px 0;
}

.tools-list a {
    color: var(--link);
}

.blog-preview-link {
    color: var(--link) !important;
    text-decoration: none;
}

.blog-preview-link h3,
.blog-preview-link p {
    color: var(--link) !important;
}

.blog-preview-link:hover {
    text-decoration: underline;
}


/* Social cards - bottom middle/right */
.social-section {
    grid-area: social;
    display: flex;
    flex-direction: column;
    gap: 15px;
    padding: 0;
    align-items: stretch;
}

.social-card {
    display: flex;
    align-items: center;
    padding: 15px;
    border: 1px solid var(--border);
    text-decoration: none;
    color: var(--text);
    background: transparent;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.social-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    text-decoration: none;
}

.social-image {
    width: 50px;
    height: 50px;
    margin-right: 15px;
    object-fit: cover;
}

.social-image-placeholder {
    width: 50px;
    height: 50px;
    background: var(--border);
    margin-right: 15px;
}

.social-title {
    margin: 0 0 5px 0;
    font-size: 1.1rem;
    font-weight: 600;
}

.social-description {
    margin: 0;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.4;
}

/* Responsive design */
@media (max-width: 1200px) {
    .homepage-container {
        grid-template-areas: 
            "sidebar hero social";
        grid-template-columns: 280px 1fr 280px;
        grid-template-rows: 1fr;
        gap: 10px;
        padding-top: 3px;
        padding-left: 15px;
        padding-right: 15px;
    }
    
    .hero-section {
        padding: 0;
    }
    
    .sidebar-left {
        padding: 0;
    }
    
    .social-section {
        padding: 0;
    }
    
}

@media (max-width: 768px) {
    .homepage-container {
        grid-template-areas: 
            "hero"
            "sidebar"
            "social";
        grid-template-columns: 1fr;
        padding: 3px 20px 20px 20px;
    }
    
    
    .nav-container {
        padding: 3px 20px;
    }
    
    .social-section {
        grid-template-columns: 1fr;
    }
}

/* Other page layouts */
h1, h2, h3, h4 {
    color: var(--text);
}

.work-section {
    margin: 20px 0;
    padding: 20px;
    border: 1px solid var(--border);
    background: var(--highlight);
    color: var(--text);
}

.work-section p, .work-section li {
    color: var(--text);
}

.work-title {
    font-size: 1.8rem;
    font-weight: 600;
    margin: 0 0 10px 0;
}

.work-subtitle {
    font-size: 1rem;
    font-style: italic;
    color: var(--text);
    margin: 0 0 15px 0;
}


.blog-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin: 0 0 5px 0;
}

.blog-date {
    font-size: 0.8em;
    color: var(--text);
}

/* Non-homepage layouts */
.container:not(.homepage-container) {
    max-width: 1200px;
    margin: 0 auto;
    padding: 100px 20px 20px 20px;
    height: auto;
    min-height: calc(100vh - 120px);
}

/* Utility classes */
.w-full {
    width: 100%;
}

.mt-4 {
    margin-top: 1rem;
}

.p-2 {
    padding: 0.5rem;
}

.p-4 {
    padding: 1rem;
}

.border {
    border: 1px solid var(--border);
}

.text-red-600 {
    color: red;
}

.border-red-600 {
    border-color: red;
}

/* Theme variables */
:root.light-theme {
    --background: #ffffff;
    --text: #000000;
    --link: #0066cc;
    --highlight: #f5f5f5;
    --border: #333333;
}

:root:not(.light-theme) {
    --background: #000000;
    --text: #ffffff;
    --link: #4da6ff;
    --highlight: #333333;
    --border: #555555;
}
"""