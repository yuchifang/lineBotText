
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


line_bot_api = LineBotApi('B33NWQ6beadplQSSM7j+Z2K5NS8j2JI8Zk/9F/O1bneKMt5kU1IWgZjHiKaNs59YabLp2ttACix3Hw6sCemR3Ef+zwmqFHk060iie6t/IAo09rBlqPSTghuoPm+KRnfok0n5M5bBeeB35MinOzzZgQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9738592ff5d8c34a8af5e033c05bd9c8')


import json

def lambda_handler(event, context):
    @handler.add(MessageEvent,message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

    signature = event['headers']['X-Line-Signature']
    body = event['body']
    try:
        handler.handle(body, signature) 
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps('Invalid signature. Please check your channel access token/channel secret.')
        }
    return {
        'statusCode':200,
        'body': json.dumps("Hello from Lambda!")
    }