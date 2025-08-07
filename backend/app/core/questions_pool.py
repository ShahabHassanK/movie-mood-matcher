# backend/app/core/questions_pool.py
QUESTION_POOL = [
    {
        "question": "How are you feeling right now?",
        "options": {
            "Happy and energetic ⚡": ["mood_happy", "pacing_fast"],
            "Thoughtful and introspective 🧘": ["mood_calm", "tone_thoughtful"],
            "Romantic and dreamy 💭": ["mood_romantic", "tone_light"],
            "Nostalgic and sentimental 📻": ["mood_nostalgic", "pacing_slow"],
            "Dark and brooding 🌑": ["tone_dark", "mood_sad"],
            "Adventurous and bold 🗺️": ["mood_excited", "genre_adventure"]
        }
    },
    {
        "question": "What's your ideal movie pace?",
        "options": {
            "Fast and intense 🚀": ["pacing_fast", "mood_excited"],
            "Slow and meditative 🐢": ["pacing_slow", "tone_thoughtful"],
            "Variable with surprises 🎭": ["pacing_variable"],
            "Steady with gradual build 🏗️": ["pacing_medium"]
        }
    },
    {
        "question": "Choose your cinematic atmosphere:",
        "options": {
            "Dark and gritty streets 🌆": ["tone_dark", "setting_urban"],
            "Sunny and colorful 🌈": ["tone_light", "mood_happy"],
            "Mysterious and foggy 🌫️": ["tone_suspenseful", "genre_mystery"],
            "High-tech neon lights 🌃": ["setting_future", "tone_gritty"]
        }
    },
    {
        "question": "Pick your perfect movie world:",
        "options": {
            "Futuristic cityscape 🏙️": ["setting_future", "genre_sci_fi"],
            "Medieval fantasy kingdom 🏰": ["setting_fantasy", "genre_fantasy"],
            "1950s small town 🏡": ["setting_historical", "mood_nostalgic"],
            "Present-day metropolis 🌇": ["setting_urban", "tone_realistic"]
        }
    },
    {
        "question": "Which story theme speaks to you?",
        "options": {
            "Love conquers all 💘": ["theme_love", "mood_romantic"],
            "Against all odds 🏆": ["theme_redemption", "tone_uplifting"],
            "Dark family secrets 🤫": ["theme_family", "tone_dark"],
            "Technological revolution ⚙️": ["theme_technology", "setting_future"]
        }
    },
    {
        "question": "What genre mood are you in?",
        "options": {
            "Laugh-out-loud funny 🤣": ["genre_comedy", "mood_happy"],
            "Edge-of-your-seat tense 😰": ["genre_thriller", "tone_suspenseful"],
            "Visually stunning fantasy ✨": ["genre_fantasy", "tone_whimsical"],
            "Thought-provoking drama 💭": ["genre_drama", "tone_thoughtful"]
        }
    },
    {
        "question": "Your ideal movie ending:",
        "options": {
            "Bittersweet and real 🍷": ["tone_bleak", "mood_sentimental"],
            "Happy and satisfying 🎊": ["tone_uplifting", "mood_happy"],
            "Mind-blowing twist 🤯": ["tone_suspenseful", "pacing_fast"],
            "Open to interpretation ❓": ["tone_thoughtful", "pacing_slow"]
        }
    },
    {
        "question": "Choose your protagonist:",
        "options": {
            "Reluctant hero 🦸": ["theme_redemption"],
            "Brilliant outcast 🧠": ["theme_identity"],
            "Rebellious spirit ✊": ["theme_rebellion"],
            "Hopeless romantic 🌹": ["mood_romantic", "theme_love"]
        }
    },
    {
        "question": "What visual style excites you?",
        "options": {
            "Vibrant animation 🎨": ["genre_animation", "tone_light"],
            "Gritty realism 🎥": ["tone_realistic", "setting_urban"],
            "Stylized noir 🕶️": ["tone_dark", "setting_historical"],
            "Futuristic CGI 🌌": ["setting_future", "genre_sci_fi"]
        }
    },
    {
        "question": "Pick a time period:",
        "options": {
            "Distant past 🏺": ["setting_historical"],
            "Retro 20th century 📻": ["setting_historical", "mood_nostalgic"],
            "Present day 📱": ["setting_modern"],
            "Imagined future 🚀": ["setting_future"]
        }
    },
    {
        "question": "How cerebral do you want it?",
        "options": {
            "Purely entertaining 🍿": ["tone_light", "mood_happy"],
            "Thought-provoking 🤔": ["tone_thoughtful"],
            "Mind-bending 🌀": ["tone_suspenseful", "genre_mystery"],
            "Philosophical deep dive 📚": ["tone_serious", "theme_morality"]
        }
    },
    {
        "question": "What relationship dynamic interests you?",
        "options": {
            "Epic romance ❤️": ["mood_romantic", "theme_love"],
            "Complex family 👨‍👩‍👧‍👦": ["theme_family", "genre_drama"],
            "Buddy adventure 👫": ["theme_friendship", "genre_adventure"],
            "Fierce rivalry ⚔️": ["theme_revenge", "tone_dark"]
        }
    },
    {
        "question": "Choose your conflict type:",
        "options": {
            "Internal struggle 🧠": ["theme_identity", "genre_drama"],
            "Physical battle 🥊": ["genre_action", "pacing_fast"],
            "Supernatural threat 👻": ["genre_horror", "tone_dark"],
            "Social/political ⚖️": ["theme_justice", "tone_serious"]
        }
    },
    {
        "question": "What viewing experience do you want?",
        "options": {
            "Cathartic cry 😭": ["mood_sad", "genre_drama"],
            "Edge-of-seat thrill 🎢": ["genre_thriller", "pacing_fast"],
            "Warm comfort blanket 🛋️": ["mood_comfy", "tone_light"],
            "Mind-expanding journey 🌌": ["genre_sci_fi", "tone_thoughtful"]
        }
    },
    {
        "question": "Pick a storytelling style:",
        "options": {
            "Classic linear narrative 📜": [],
            "Non-chronological puzzle 🧩": ["pacing_variable"],
            "Anthology of stories 📚": [],
            "Experimental/artsy 🎨": []
        }
    },
    {
        "question": "How important is realism?",
        "options": {
            "Documentary-level real 📹": ["tone_realistic", "genre_documentary"],
            "Grounded but fictional 🏠": ["tone_realistic"],
            "Magical/supernatural ✨": ["genre_fantasy", "tone_whimsical"],
            "Sci-fi futuristic 🤖": ["genre_sci_fi", "setting_future"]
        }
    },
    {
        "question": "What's your ideal runtime?",
        "options": {
            "Quick 90 minutes ⏳": ["pacing_fast"],
            "Standard 2 hours 🕑": [],
            "Epic 3+ hours 🏛️": ["pacing_slow"],
            "No preference 🤷": []
        }
    },
    {
        "question": "Choose a color palette:",
        "options": {
            "Warm and golden ☀️": ["tone_light", "mood_happy"],
            "Cool and blue ❄️": ["tone_thoughtful", "mood_calm"],
            "Dark and shadowy 🌑": ["tone_dark", "genre_horror"],
            "Neon and vibrant 🌈": ["setting_future", "tone_gritty"]
        }
    },
    {
        "question": "What musical vibe do you want?",
        "options": {
            "Orchestral epic 🎻": ["tone_epic", "genre_fantasy"],
            "Synthwave retro 📻": ["setting_future", "mood_nostalgic"],
            "Minimal ambient 🎧": ["tone_thoughtful", "pacing_slow"],
            "Popular soundtrack 🎶": ["tone_light", "mood_happy"]
        }
    },
    {
        "question": "How should it challenge you?",
        "options": {
            "Moral dilemmas ⚖️": ["theme_morality", "tone_serious"],
            "Complex plot 🧩": ["genre_mystery", "tone_suspenseful"],
            "Emotional depth 💔": ["genre_drama", "mood_sad"],
            "Visual symbolism 🎨": ["tone_thoughtful", "pacing_slow"]
        }
    },
    {
        "question": "Pick a director's style:",
        "options": {
            "Wes Anderson whimsy 🎩": ["tone_whimsical", "genre_comedy"],
            "Christopher Nolan mind-bender 🌀": ["tone_suspenseful", "genre_sci_fi"],
            "Greta Gerwig heartfelt ✨": ["tone_uplifting", "genre_drama"],
            "Guillermo del Toro dark fantasy 🦇": ["tone_dark", "genre_fantasy"]
        }
    },
    {
        "question": "What cultural perspective?",
        "options": {
            "Hollywood blockbuster 🎥": [],
            "European arthouse 🎭": [],
            "Asian cinema 🏯": [],
            "Global/international 🌍": []
        }
    },
    {
        "question": "How dialogue-heavy?",
        "options": {
            "Talky and philosophical 💬": ["tone_thoughtful", "pacing_slow"],
            "Balanced mix ↔️": [],
            "Visual/action-focused 🎬": ["pacing_fast", "genre_action"],
            "Minimal/subtle 🤫": ["tone_bleak", "pacing_slow"]
        }
    },
    {
        "question": "Choose your viewing time:",
        "options": {
            "Morning inspiration 🌅": ["tone_uplifting", "mood_happy"],
            "Afternoon escape 🏖️": ["tone_light", "mood_comfy"],
            "Late night thrill 🌃": ["genre_thriller", "tone_dark"],
            "Marathon weekend 🍿": ["pacing_slow", "tone_epic"]
        }
    },
    {
        "question": "What character growth appeals?",
        "options": {
            "Rags to riches 📈": ["theme_redemption"],
            "Coming of age 👦→👨": ["theme_coming_of_age"],
            "Antihero's journey 🖤": ["tone_dark", "theme_redemption"],
            "Self-discovery 🧭": ["theme_identity", "tone_thoughtful"]
        }
    },
    {
        "question": "Pick a narrative scope:",
        "options": {
            "Intimate character study 👤": ["genre_drama", "pacing_slow"],
            "Ensemble cast 🌟": [],
            "World-changing events 🌎": ["tone_epic", "pacing_fast"],
            "Generational saga 👨‍👩‍👧‍👦": ["setting_historical", "pacing_slow"]
        }
    },
    {
        "question": "How experimental can it be?",
        "options": {
            "Mainstream conventional 🏙️": [],
            "Slightly unconventional 🎨": [],
            "Avant-garde weird 🌀": [],
            "No limits 🚀": []
        }
    },
    {
        "question": "What emotional intensity?",
        "options": {
            "Gentle and mild 🌱": ["tone_light", "mood_calm"],
            "Moderate and engaging 🎭": [],
            "Powerful and moving 💥": ["genre_drama", "mood_sad"],
            "Overwhelmingly intense 🌪️": ["genre_horror", "tone_dark"]
        }
    },
    {
        "question": "Choose your humor style:",
        "options": {
            "Witty dialogue 💬": ["genre_comedy", "tone_light"],
            "Slapstick physical 🤹": ["genre_comedy", "mood_happy"],
            "Dark/satirical ☠️": ["genre_comedy", "tone_dark"],
            "No humor please 😐": []
        }
    },
    {
        "question": "How important is happy ending?",
        "options": {
            "Essential for me 😊": ["tone_uplifting", "mood_happy"],
            "Prefer but not required 🙂": [],
            "Bittersweet is fine 🍷": ["mood_sentimental"],
            "Give me tragedy 😭": ["mood_sad", "tone_bleak"]
        }
    },
    {
        "question": "What's your age preference?",
        "options": {
            "Family friendly 👨‍👩‍👧‍👦": ["tone_light", "mood_happy"],
            "Teen/young adult 🎓": ["theme_coming_of_age"],
            "Adult themes 🔞": ["tone_dark"],
            "No preference 🤷": []
        }
    },
    {
        "question": "How familiar should it feel?",
        "options": {
            "Comfortably familiar 🛋️": ["mood_comfy", "mood_nostalgic"],
            "New twist on classics 🔄": [],
            "Completely original 💡": [],
            "Challenge my expectations 🤯": ["tone_suspenseful", "pacing_variable"]
        }
    },
    {
        "question": "Pick a production era:",
        "options": {
            "Classic (pre-1970) 🎩": ["setting_historical", "mood_nostalgic"],
            "80s/90s retro 📼": ["mood_nostalgic"],
            "Modern 2000s 📱": [],
            "Recent release 🆕": []
        }
    },
    {
        "question": "What rating intensity?",
        "options": {
            "PG family fun 👪": ["tone_light", "mood_happy"],
            "PG-13 thrills 🎢": [],
            "R-rated edge 🔪": ["tone_dark", "genre_horror"],
            "No limits/unrated 🔥": []
        }
    }
]