# MCRCON-webhook
マインクラフトサーバーの入退室履歴をDiscordにWebhookを利用して通知します。

# リリース
すべてのリリースは以下の場所にあります。

・github：https://github.com/yukugura/MCRCON-webhook/releases/

# How to use

## 手順１
**MCRCON-webhook.py**プログラム冒頭に監視する**サーバーIP**、**ポート番号**、**RCONパスワード**、**Webhook-URL**の４つを変数として宣言しています。利用する環境に合わせて変更してください。

初期の段階では以下のように宣言しています。
サーバーIP：localhost
RCONポート：25575
RCONパス：password
webhook_url：https://discord.com/api/webhooks/xxxxxxxx

## 手順２
監視するマインクラフトサーバー側の設定を変更します。
初期段階のマインクラフトサーバーだと、RCONの使用が許可されていないため設定を変更し適用する必要があります。
サーバーディレクトリ内の**「server.properties」**ファイルを任意のテキストエディタで編集します。
![server-file](https://github.com/user-attachments/assets/0e61f2ab-14d0-4e0a-a0cc-e0e0c22eea58)

**赤色矢印**で示した**３つの箇所**を変更してください。
※画像の設定値は、初期宣言と同じ内容を設定した場合のものです。

`enable-rcon=false` ▶ `enable-rcon=true`

`rcon.password=` ▶ `rcon.password=<任意のパスワード>`

`rcon.port=25575` ▶ `rcon.port=<任意のポート番号>`

![server-properties](https://github.com/user-attachments/assets/93e18df4-d5db-43fa-a84d-12428be50461)

## 手順３
**Python3**のインストールと必要ライブラリのインストールを行います。
※すでに実行環境がある場合、「手順３」は不要です。
**Python3**を[公式サイト](https://www.python.org/downloads/)よりダウンロードしインストール。
コマンドプロンプトを起動し、以下のコマンドでライブラリをインストールします。
`pip install requests`
`pip install mcrcon`

# ライセンス
このプロジェクトは **MITライセンス** の下で公開されています。詳細については、リポジトリ内の [LICENSE](https://github.com/yukugura/MCRCON-webhook/blob/main/LICENSE) ファイルをご覧ください。

Thank you for [Contributors](https://github.com/yukugura/MCRCON-webhook/graphs/contributors)
