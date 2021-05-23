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

## デプロイ

本番環境へのデプロイ方法は色々選択肢があるが、AWSの「[App Runner](https://aws.amazon.com/jp/blogs/news/app-runner-from-code-to-scalable-secure-web-apps/)」というコンテナ管理サービスを使うとほとんど何も考えずにデプロイできるので楽。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f62623432353534622d646233342d613937382d653736312d6335363834306133306233632e706e67](https://user-images.githubusercontent.com/51913879/119265925-9edb9500-bc23-11eb-88ba-14224863fe57.png)

参照記事: [What is AWS App Runner?](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)

※ごちゃごちゃ説明するよりも実際に手を動かしたほうがわかりやすいと思うので、以下の通りの手順を試してみてください。（もしAWSアカウントをまだ持っていない場合は事前に準備をお願いします。）

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f39653739623431342d653633302d323739312d346636612d3736373365373831333739332e6a706567](https://user-images.githubusercontent.com/51913879/119266073-41941380-bc24-11eb-8615-dc2791889391.jpeg)

AWSコンソール画面から「App Runner」を探し出し、「サービスを作成」をクリック。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f35376364623663342d623839322d346439342d356262352d3163316565313738363930302e6a706567](https://user-images.githubusercontent.com/51913879/119266134-8a4bcc80-bc24-11eb-8a99-0f4873ffb6cd.jpeg)

リポジトリタイプは「ソースコードリポジトリ」を選び、GitGubとの接続を行うために「新規追加」をクリック。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f30623464366334612d646463352d313333312d633735392d6562646536353932346132362e6a706567](https://user-images.githubusercontent.com/51913879/119266171-b49d8a00-bc24-11eb-886a-79d9f8b3cfe4.jpeg)

接続名を適当に入力し、「別のアプリケーションをインストールする」をクリック。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f35653565396533312d383830322d303563382d353235652d3963666366313563633532382e6a706567](https://user-images.githubusercontent.com/51913879/119266231-e4e52880-bc24-11eb-8a36-df69057da4e7.jpeg)

どのGitHubアカウントにコネクターをインストールするか選択。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f61636336313132372d663639372d346464612d393963362d6134623639626665636165622e6a706567](https://user-images.githubusercontent.com/51913879/119266310-3e4d5780-bc25-11eb-8466-dadd82a6f771.jpeg)

「All repositories（全てのリポジトリ）」を対象にするか、「Onle select repositories（選択したリポジトリ一つだけ）」を対象にするか聞かれますが、今回は「All repositories」を選択。

![68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3638383835342f63336265383062312d376630642d396234322d303366392d6366663231373661386237612e6a706567](https://user-images.githubusercontent.com/51913879/119266278-16f68a80-bc25-11eb-96db-f77a15cb7e8f.jpeg)

接続に成功すると、先ほどは空欄だった「GitHubアプリケーション」の欄にGitHubアカウント名が追加されるので、このまま「次へ」をクリック。

![スクリーンショット 2021-05-24 0 18 07_censored](https://user-images.githubusercontent.com/51913879/119266387-92f0d280-bc25-11eb-8b09-b29ad6a542e9.jpg)

- リポジトリ
  - デプロイしたいBotのソースコードを含むGitHubリポジトリ
- ブランチ
  - そのコードが含まれるブランチ
- デプロイ設定
  - お好み（自動にしていると$1/月のコストがかかるので注意）

![スクリーンショット 2021-05-24 0 25 00_censored](https://user-images.githubusercontent.com/51913879/119266628-8456eb00-bc26-11eb-816b-01c0a8395d59.jpg)

- 設定ファイル
  - ここですべての設定を構成する
- ランタイム
  - Python3
- 構築コマンド
  - pip install -r requirements.txt
- 開始コマンド
  - sh exec_job.sh
- ポート
  - 8000

![スクリーンショット 2021-05-24 0 27 45_censored](https://user-images.githubusercontent.com/51913879/119266746-f62f3480-bc26-11eb-8b1a-044e1c963eba.jpg)


- サービス名
  - 任意
- 環境変数
  - 適宜入力
- その他
  - 特にいじらずデフォルトのままでOK

![スクリーンショット 2021-05-24 0 30 56_censored](https://user-images.githubusercontent.com/51913879/119266838-5625db00-bc27-11eb-9e10-849464072795.jpg)

最後に諸々の確認画面が出てくるので、問題無さそうなら一番下にある「作成とデプロイ」をクリック。

![スクリーンショット 2021-05-24 0 33 14_censored](https://user-images.githubusercontent.com/51913879/119266927-aac95600-bc27-11eb-8ab6-e385e6db19a2.jpg)

するとこんな感じでデプロイが始まるので、完了するまで少し待ちましょう。大体５分前後で終わると思います。

![スクリーンショット 2021-05-24 0 37 35_censored (1)](https://user-images.githubusercontent.com/51913879/119267216-85891780-bc28-11eb-8d4f-3a4f4e14a658.jpg)

無事成功したら、表示されているドメインにアクセスしてみましょう。

<img width="521" alt="スクリーンショット 2021-05-24 0 53 23" src="https://user-images.githubusercontent.com/51913879/119267633-73a87400-bc2a-11eb-90d7-6e43f548d873.png">

ちゃんとデプロイできているかどうか確認。

<img width="395" alt="スクリーンショット 2021-05-24 0 51 00" src="https://user-images.githubusercontent.com/51913879/119267552-1e6c6280-bc2a-11eb-9aaa-f42879fee731.png">

LINE通知も届いていれば無事Botの稼働に成功です。

![スクリーンショット 2021-05-24 0 56 05_censored](https://user-images.githubusercontent.com/51913879/119267753-df8adc80-bc2a-11eb-85ca-a5e03024cae7.jpg)

一時的に停止したい場合や完全に削除したい場合は右上の「アクション」から。

### 注意点

App Runnerはその可用性を担保するために、一定の間隔でヘルスチェック（あらかじめ決めたURLにアクセスを送り、正しいレスポンスが返ってくるかどうか確認）を行っています。そのアクセスを待ち構えるフロント部分のページが必要となるため、「index.html」ファイルは必須になります。

また、同時にWebサーバーも立てておく必要があるため、「 $ python -m http.server」コマンドを実行しなければなりません。その辺は「exec_job.sh」ファイル内に記載してあるので、ポート番号を変更したい場合などはそちらを適宜変更してください。


