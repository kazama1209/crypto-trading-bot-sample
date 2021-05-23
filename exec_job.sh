#!/bin/bash
# Webサーバーを起動してフロント部分を表示させる一方、バックグラウンドでBotを作動
python -m http.server 8000 | python main.py
