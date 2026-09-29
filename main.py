import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


@app.route("/")
def home():
    return "PocketSmart AI is running!"


@app.route("/ask", methods=["POST"])
def ask_gemini():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Please enter a message."}), 400

    if model is None:
        return jsonify({
            "response": "Gemini API key is not configured yet."
        })

    response = model.generate_content(user_input)

    return jsonify({
        "response": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)
