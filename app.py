from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

@app.route("/", methods=["GET"])
def home():
    return "Engagera backend is running!"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data.get("message", "").lower()

    if "hello" in user:
        reply = "Hello Abdul ☺️"
    elif "game" in user:
        reply = "Let's build a game"
    elif "ai" in user:
        reply = "AI is the future"
    else:
        reply = "That sounds interesting... tell me more."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
