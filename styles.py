BASE_STYLES = """
    :root {
        --neon-blue: #00fff2;
        --neon-pink: #ff00ff;
        --neon-purple: #bc13fe;
        --dark-bg: #0c1e2e;      
        --darker-bg: #061625;    
        --accent-blue: #0066cc;  
        --card-bg: rgba(20, 35, 60, 0.85);
        --text-color: #fff;
    }

    @keyframes subtle-shift {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }

    :root.light-theme {
        --neon-blue: #ff00ff;
        --neon-pink: #00ff00;
        --neon-purple: #ffff00;
        --dark-bg: #ffffff;
        --darker-bg: #f0f0f0;
        --accent-blue: #ff0000;
        --card-bg: rgba(255, 255, 255, 0.85);
        --text-color: #000;
    }

    @keyframes gradient-zoom {
        0% {
            transform: scale(1) rotate(0deg);
            background-size: 400% 400%;
            background-position: 0% 50%;
        }
        25% {
            transform: scale(1.5) rotate(90deg);
            background-size: 200% 200%;
            background-position: 100% 50%;
        }
        50% {
            transform: scale(1) rotate(180deg);
            background-size: 400% 400%;
            background-position: 50% 100%;
        }
        75% {
            transform: scale(1.5) rotate(270deg);
            background-size: 200% 200%;
            background-position: 50% 0%;
        }
        100% {
            transform: scale(1) rotate(360deg);
            background-size: 400% 400%;
            background-position: 0% 50%;
        }
    }

    :root.light-theme body {
        position: relative; /* Ensure the body is relative to position the background */
        overflow: hidden; /* Prevent scrollbars if the background overflows */
    }

    :root.light-theme body::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            45deg, 
            #ff0000,
            #ff00ff,
            #00ff00,
            #ffff00,
            #00ffff,
            #ff0000
        );
        background-size: 400% 400%;
        animation: gradient-zoom 10s infinite linear;
        transform-origin: center center;
        z-index: 0; /* Ensure the background is below the content */
    }

    :root.light-theme .container {
        position: relative;
        z-index: 1; /* Ensure the content is above the background */
    }


    .theme-toggle {
        padding: 0.5rem 1rem;
        border: 1px solid var(--neon-blue);
        border-radius: 4px;
        background: transparent;
        color: var(--text-color);
        cursor: pointer;
        transition: all 0.3s;
        font-size: 0.9rem;
        text-shadow: 0 0 5px var(--neon-blue);
        margin: 0 0.25rem;
    }

    .theme-toggle:hover {
        background: var(--neon-blue);
        color: var(--dark-bg);
        box-shadow: 0 0 15px var(--neon-blue);
        text-shadow: none;
    }

    body {
        color: #fff;
        font-family: 'Segoe UI', system-ui, sans-serif;
        margin: 0;
        min-height: 100vh;
        background: radial-gradient(
            circle at top right,
            rgba(0, 102, 204, 0.15),
            var(--dark-bg) 50%,
            var(--darker-bg) 100%
        );
        background-size: 200% 200%;
        animation: subtle-shift 15s ease infinite;
    }

    .container {
        max-width: 60rem;
        margin: 2rem auto;
        padding: 0 2rem;
    }

    .nav-item {
        color: #fff;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border: 1px solid var(--neon-blue);
        border-radius: 4px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s;
        margin: 0 0.25rem;
        text-shadow: 0 0 5px var(--neon-blue);
        font-size: 0.9rem;
        white-space: nowrap;
    }

    .nav-item:hover {
        background: var(--neon-blue);
        color: var(--dark-bg);
        box-shadow: 0 0 15px var(--neon-blue);
        text-shadow: none;
    }

    .nav-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
        gap: 0.5rem;
        flex-wrap: nowrap;
        padding: 0 0.5rem;
    }

    .social-card {
        background: var(--card-bg);
        border: 1px solid var(--neon-purple);
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s;
        display: flex;
        align-items: center;
        text-decoration: none;
        color: #fff;
        backdrop-filter: blur(10px);
    }

    .social-card:hover {
        box-shadow: 0 0 20px var(--neon-purple);
        transform: translateY(-2px);
    }

    .social-image {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin-right: 1.5rem;
        border: 2px solid var(--neon-pink);
        transition: all 0.3s;
        object-fit: cover;
        background: var(--card-bg);
    }

    .social-card:hover .social-image {
        border-color: var(--neon-purple);
        box-shadow: 0 0 15px var(--neon-purple);
    }

    h1 {
        font-size: 3rem;
        text-align: center;
        margin: 2rem 0;
        background: linear-gradient(45deg, var(--neon-blue), var(--neon-pink));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(0, 255, 242, 0.5);
    }

    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }

    .profile-image {
        display: block;
        margin: 2rem auto;
        border-radius: 12px;
        border: 2px solid var(--neon-blue);
        box-shadow: 0 0 20px var(--neon-blue);
        max-width: 100%;
        height: auto;
        object-fit: cover;
    }

    .blog-card {
        /* existing styles */
        display: block;  /* Add this */
        word-break: normal;  /* Add this */
        overflow-wrap: break-word;  /* Add this */
    }

    .blog-card:hover {
        box-shadow: 0 0 20px var(--neon-blue);
        transform: translateY(-2px);
    }

    .blog-title {
        /* existing styles */
        word-break: normal;  /* Add this */
        line-height: 1.3;  /* Add this for better readability */
        max-width: 100%;  /* Add this */
    }

    .blog-date {
        /* existing styles */
        display: block;  /* Add this */
    }

    .work-section {
        background: var(--card-bg);
        border: 1px solid var(--neon-pink);
        border-radius: 8px;
        padding: 2rem;
        margin: 2rem 0;
    }

    .work-title {
        color: var(--neon-pink);
        margin: 0;
        font-size: 1.8rem;
    }

    .work-subtitle {
        color: #888;
        font-size: 1rem;
        margin: 0.5rem 0 1.5rem 0;
    }

    @media (max-width: 768px) {
        .container {
            padding: 0 0.5rem;
        }
        
        .nav-item {
            padding: 0.4rem 0.75rem;
            font-size: 0.85rem;
        }

        .social-card {
            flex-direction: column;
            text-align: center;
        }
        
        .social-image {
            margin: 0 0 1rem 0;
        }

        h1 {
            font-size: 2.5rem;
        }
    }

    @media (max-width: 380px) {
        .nav-item {
            padding: 0.3rem 0.5rem;
            font-size: 0.8rem;
        }
    }

    img {
        opacity: 1;
        transition: opacity 0.3s ease-in-out;
    }

    img.loading {
        opacity: 0;
    }

    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;  /* Ensure vertical alignment */
        margin: 2rem 0;
        gap: 0.5rem;
        flex-wrap: nowrap;
        padding: 0 0.5rem;
        position: relative;  /* For absolute positioning reference */
    }

    .nav-item.active {
    background: var(--neon-pink);
    color: var(--dark-bg);
    box-shadow: 0 0 15px var(--neon-pink);
    text-shadow: none;
}
"""
