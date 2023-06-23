from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from config.config import LineConfig

# Line Bot config
# your access token to line bot which get from line biz
accessToken = LineConfig.ACCESS_TOKEN
# your secret token to access line bot webhook get from line developer
secret = LineConfig.SERCRET

class LineMessage():

    @classmethod
    def send(cls, event, messages):
        line_bot_api = LineBotApi(accessToken)
        handler = WebhookHandler(secret)
        replyToken = event.reply_token
        echoMessages = TextSendMessage(text=messages)
        line_bot_api.reply_message(
            reply_token=replyToken, messages=echoMessages)


