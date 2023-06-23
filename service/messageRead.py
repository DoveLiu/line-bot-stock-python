from spider.YahooStock import YahooStock
from service.line.LineMessage import LineMessage

class messageRead():
    # def __init__(self):
    #     pass

    @classmethod    
    def switch(cls, event, message:str):
        # print(message)
        if message.startswith('/s'):
            stock_symbol = message[2:]
            stock_info = YahooStock.get_stock_info(stock_symbol)
            if not stock_info:
                return
            LineMessage.send(event, stock_info)
            print('stock_info\n' + stock_info)
