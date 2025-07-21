import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    send_message("🚀 Bot is live on Render and ready to send you signals!")
    while True:
        send_message("📈 Sample Signal: BTCUSDT Long @ $62,000, SL: $61,000, TP: $65,000")
        time.sleep(3600)
