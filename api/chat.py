import json

def handler(request):
    if request.method == "POST":
        body = request.get_json()
        user = body.get("message", "").lower()

        if "hello" in user:
            reply = "Hello Abdul ☺️"
        elif "game" in user:
            reply = "Let's build a game"
        elif "ai" in user:
            reply = "AI is the future"
        else:
            reply = "That sounds interesting... tell me more."

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"response": reply})
        }

    return {
        "statusCode": 405,
        "body": "Method Not Allowed"
    }
