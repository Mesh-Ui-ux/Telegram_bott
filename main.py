import requests
import time
import os
import threading
from flask import Flask

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

# Background bot logic
def start_bot():
    send_message("🚀 Bot is live on Render and ready to send you signals!")
    while True:
        send_message("📈 Sample Signal: BTCUSDT Long @ $62,000, SL: $61,000, TP: $65,000")
        time.sleep(3600)

# Start bot in separate thread
threading.Thread(target=start_bot).start()

# Dummy web server to keep Render happy
app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
