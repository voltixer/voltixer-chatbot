from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "سلام": "سلام! چطور می‌تونم کمکت کنم؟",
    "اسمت چیه؟": "من یک چت‌بات ساده‌ام، تو می‌تونی منو VoltixerBot صدا کنی!",
    "خداحافظ": "فعلاً خداحافظ :)",
    "چه کارهایی بلدی؟": "من می‌تونم به سوالات ساده پاسخ بدم!"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    answer = responses.get(user_message, "متأسفم، متوجه نشدم. لطفاً واضح‌تر بپرس.")
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
