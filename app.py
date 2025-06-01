from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

@app.route('/')
def home():
    return "Telegram Bot Backend is running."

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data.get('chat_id')
    text = data.get('text')

    if not chat_id or not text:
        return {"error": "Missing chat_id or text"}, 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
