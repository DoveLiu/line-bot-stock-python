import os
import uvicorn
from fastapi import FastAPI, Request, HTTPException

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from config.config import Config, LineConfig
from service.messageRead import messageRead
# from spider.stickershopToExcel import stickers

# Line Bot config
# your access token to line bot which get from line biz
accessToken = LineConfig.ACCESS_TOKEN
# your secret token to access line bot webhook get from line developer
secret = LineConfig.SERCRET

app = FastAPI()

line_bot_api = LineBotApi(accessToken)
handler = WebhookHandler(secret)

@app.get("/")
def root():

    return{"hello":"world"}

@app.post("/callback")
async def echoBot(request: Request):
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    try:
        # 使用 handler 物件處理接收到的 Line Bot 事件。它接受解碼後的請求主體和簽名作為參數，並執行相應的處理邏輯。
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    return "OK"


@handler.add(MessageEvent, message=(TextMessage))
def handling_message(event):
    replyToken = event.reply_token
    print(event.message)
    if isinstance(event.message, TextMessage):
        # 使用者發的訊息
        messages = event.message.text
        messageRead.switch(event, messages)
        # echoMessages = TextSendMessage(text=messages)
        # line_bot_api.reply_message(
        #     reply_token=replyToken, messages=echoMessages)


if __name__ == '__main__':
    server_port = int(os.environ.get('PORT', Config.PORT))
    uvicorn.run(app, host=Config.HOST, port=server_port, log_level="info")