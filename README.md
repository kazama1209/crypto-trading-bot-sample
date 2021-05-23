# crypto-trading-bot-sample

仮想通貨自動売買Botのサンプル。

※１分足のゴールデンクロス・デッドクロス（短期移動平均線と長期移動平均線のクロス）に反応してドテン売買を繰り返すという非常に雑なロジックのBotなので、本番運用ではまず勝てません。ただ単にBotの仕組み（作り方や動かし方）を理解するためのものくらいに考えてください。

## セットアップ

必要なライブラリをインストール。

```
$ pip install -r requirements.txt
```

環境変数をセット。

```
$ cp .env.sample .env

API_KEY=<Bybit APIキー>
SECRET=<Bybit シークレット>
LINE_NOTIFY_TOKEN=<LINE Notify トークン>
```

## 動作確認

Botを起動。

```
$ sh exec_job.sh
```

<img width="438" alt="スクリーンショット 2021-05-23 23 39 33" src="https://user-images.githubusercontent.com/51913879/119265022-32ab6200-bc20-11eb-8262-19fdf43959f2.png">

[http://localhost:8000](http://localhost:8000/) にアクセスして「Crypto trading bot is working successfully!」と表示されれば成功。

<img width="536" alt="スクリーンショット 2021-05-23 23 42 41" src="https://user-images.githubusercontent.com/51913879/119265124-9170db80-bc20-11eb-98aa-21331f9fac6f.png">

LINEの方にもBotが稼働し始めた事が通知されているはず。
