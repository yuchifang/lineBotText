# 載入LineBot所需要的模組
import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import data

app = Flask(__name__)

# 必須放上自己的 Channel Access Token
line_bot_api = LineBotApi(data.token)
# = find token
# 可以從 Line developer 上 = 自己的專案 = 選擇模式
# = Messaging API
# = Channel access token 點選 issue
# = 即可看到 token

# 必須放上自己的 Channel Secret
handler = WebhookHandler(data.secretCode)
# = find secret code
# = Basic setting
# = Channel secret 點選 issue
# = 即可看到 secret code


# 加上 測試程式碼
line_bot_api.push_message(data.id, TextSendMessage(text='你可以開始了'))
# find id
# = Basic setting
# = Your user ID
# = 即可看到 ID

# todo 上面部分 line 與 python 串接
# todo heroku 與 Line Bot 串接


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 進入 heroku = 選擇 = 當前的傳案 open app
# 複製 url 到 line Developer
# 點選 Messaging API =
# Webhook settings 貼上 url

# 設定 line bot 自動回訊息
# 點選 Auto-reply messages
# 將自動回訊息 設為 停用
# 將webhook 設為 啟用


print("somes")

# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


# 主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
