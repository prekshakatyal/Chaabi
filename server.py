"""
Chaabi Roops FAQ Assistant — backend (Gemini free-tier version)
-----------------------------------------------------------------
Uses Google's Gemini API instead of Anthropic's, because Gemini has a
genuinely free tier (generous limits on the Flash model, no credit card
needed) — good for building and testing this project at zero cost.

SETUP (5-10 min):
  1. pip install flask google-generativeai
  2. Get a free key at https://aistudio.google.com/apikey (see chat for steps)
  3. export GEMINI_API_KEY="AIza..."
  4. python server.py
  5. Open http://localhost:5000

CUSTOMIZE: edit faqs.json, not this file, to change the business's answers.
"""

import os
import json
from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai

app = Flask(__name__, static_folder="static")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

with open(os.path.join(os.path.dirname(__file__), "faqs.json"), encoding="utf-8") as f:
    business_data = json.load(f)

faq_text = "\n\n".join(
    f"Q: {item['question']}\nA: {item['answer']}"
    for item in business_data["faqs"]
)

SYSTEM_PROMPT = f"""You are a friendly, helpful assistant for {business_data['business_name']},
an Instagram-based small business ({business_data['tagline']}). Answer customer
questions using ONLY the information below. If a question isn't covered here
(for example, asking about stock/size availability for a specific item),
say you'll have the founder follow up personally rather than guessing.

Tone: {business_data['tone_notes']}

FAQs:
{faq_text}
"""

# gemini-2.5-flash carries the generous free-tier quota as of 2026.
model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    system_instruction=SYSTEM_PROMPT,
)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "").strip()
    history = data.get("history", [])  # list of {role, content}

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Gemini expects roles "user" / "model" (not "assistant") and a
    # "parts" list rather than a plain "content" string.
    gemini_history = [
        {
            "role": "model" if h["role"] == "assistant" else "user",
            "parts": [h["content"]],
        }
        for h in history
    ]

    chat_session = model.start_chat(history=gemini_history)
    response = chat_session.send_message(user_message)

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
