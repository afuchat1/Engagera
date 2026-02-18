import json

def handler(request, response):
    if request.method == "POST":
        body = request.json()
        user = body.get("message", "").lower()

        if "hello" in user:
            reply = "Hello Abdul ☺️"
        elif "game" in user:
            reply = "Let's build a game"
        elif "ai" in user:
            reply = "AI is the future"
        else:
            reply = "That sounds interesting... tell me more."

        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.write(json.dumps({"response": reply}))
    else:
        response.status_code = 405
        response.write("Method Not Allowed")
