import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CARDS = {
    "kai": {
        "slug": "kai",
        "name": "Kai (Tam Zhao Kai)",
        "short_name": "Kai",
        "role": "Co-Founder, Chief Marketing Officer",
        "filename": "Oser business card.png",
        "emails": ["zhaokaitam@gmail.com", "tooser.todare@gmail.com"],
        "phone": "+6016 201 4242",
        "whatsapp": "60162014242",
        "hotspots": [
            {
                "type": "email",
                "label": "Email zhaokaitam@gmail.com",
                "href": "mailto:zhaokaitam@gmail.com",
                "left": "37.8%", "top": "55.0%", "width": "34.2%", "height": "6.8%"
            },
            {
                "type": "whatsapp",
                "label": "WhatsApp +6016 201 4242",
                "href": "https://wa.me/60162014242",
                "left": "73.2%", "top": "55.0%", "width": "21.8%", "height": "6.8%"
            },
            {
                "type": "email",
                "label": "Email tooser.todare@gmail.com",
                "href": "mailto:tooser.todare@gmail.com",
                "left": "57.2%", "top": "62.8%", "width": "37.8%", "height": "6.8%"
            }
        ]
    },
    "lee-chun-hin": {
        "slug": "lee-chun-hin",
        "name": "Lee Chun Hin",
        "short_name": "Lee Chun Hin",
        "role": "Co-Founder, Chief Finance Officer",
        "filename": "Oser business card (2).png",
        "emails": ["tooser.todare@gmail.com"],
        "phone": "+6014 300 9679",
        "whatsapp": "60143009679",
        "hotspots": [
            {
                "type": "whatsapp",
                "label": "WhatsApp +6014 300 9679",
                "href": "https://wa.me/60143009679",
                "left": "71.5%", "top": "53.8%", "width": "22.5%", "height": "6.8%"
            },
            {
                "type": "email",
                "label": "Email tooser.todare@gmail.com",
                "href": "mailto:tooser.todare@gmail.com",
                "left": "56.5%", "top": "61.5%", "width": "37.8%", "height": "6.8%"
            }
        ]
    },
    "adem": {
        "slug": "adem",
        "name": "Adem (Lee Kian Yang)",
        "short_name": "Adem",
        "role": "Founder, Chief Executive Officer",
        "filename": "Oser business card (3).png",
        "emails": ["kianyanglee@yahoo.com", "tooser.todare@gmail.com"],
        "phone": "+60 17 604 6832",
        "whatsapp": "60176046832",
        "hotspots": [
            {
                "type": "email",
                "label": "Email kianyanglee@yahoo.com",
                "href": "mailto:kianyanglee@yahoo.com",
                "left": "40.5%", "top": "55.2%", "width": "31.5%", "height": "6.5%"
            },
            {
                "type": "whatsapp",
                "label": "WhatsApp +60 17 604 6832",
                "href": "https://wa.me/60176046832",
                "left": "73.8%", "top": "55.2%", "width": "20.5%", "height": "6.5%"
            },
            {
                "type": "email",
                "label": "Email tooser.todare@gmail.com",
                "href": "mailto:tooser.todare@gmail.com",
                "left": "61.5%", "top": "62.0%", "width": "32.8%", "height": "6.5%"
            }
        ]
    },
    "richard": {
        "slug": "richard",
        "name": "Richard (Tan Yih Zhe)",
        "short_name": "Richard",
        "role": "Co-Founder, Chief Technology Officer",
        "filename": "Oser business card (4).png",
        "emails": ["tooser.todare@gmail.com"],
        "phone": None,
        "whatsapp": None,
        "hotspots": [
            {
                "type": "email",
                "label": "Email tooser.todare@gmail.com",
                "href": "mailto:tooser.todare@gmail.com",
                "left": "56.5%", "top": "62.5%", "width": "37.8%", "height": "6.8%"
            }
        ]
    }
}

# Friendly URL aliases so multiple name variations work seamlessly
ALIASES = {
    "tam-zhao-kai": "kai",
    "chun-hin": "lee-chun-hin",
    "leechunhin": "lee-chun-hin",
    "lee-kian-yang": "adem",
    "kian-yang": "adem",
    "tan-yih-zhe": "richard",
    "yih-zhe": "richard"
}


@app.route("/")
def index():
    return render_template("index.html", cards=CARDS.values())


@app.route("/images/<path:filename>")
def serve_image(filename):
    # Verify filename belongs to our cards to keep serving safe
    valid_files = {c["filename"] for c in CARDS.values()}
    if filename not in valid_files:
        abort(404)
    return send_from_directory(BASE_DIR, filename)


@app.route("/<slug>")
def view_card(slug):
    key = slug.lower().strip()
    key = ALIASES.get(key, key)
    card = CARDS.get(key)
    if not card:
        abort(404)
    return render_template("card.html", card=card, all_cards=CARDS.values())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("\n========================================================")
    print("  Oser 3D Business Cards Server Running!")
    print("========================================================")
    print(f"  Directory Hub : http://localhost:{port}/")
    for slug, info in CARDS.items():
        print(f"  {info['short_name']:<13} : http://localhost:{port}/{slug}")
    print("========================================================\n")
    app.run(host="0.0.0.0", port=port, debug=False)
