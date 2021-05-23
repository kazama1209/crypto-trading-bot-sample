import requests
import os

from dotenv import load_dotenv
load_dotenv(verbose=True)

# .envから値を取得
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

class LineNotify:
    def __init__(self):
        self.line_notify_token = LINE_NOTIFY_TOKEN
        self.line_notify_api = "https://notify-api.line.me/api/notify"
        self.headers = {
          "Authorization": f"Bearer {self.line_notify_token}"
        }

    def send(self, msg):
        msg = { "message": f" {msg}" }
        requests.post(self.line_notify_api, headers = self.headers, data = msg)
