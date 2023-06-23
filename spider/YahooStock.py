import requests
from lxml import etree

class YahooStock():

    @classmethod    
    def get_stock_info(cls, stock_symbol):
        url = "https://tw.stock.yahoo.com/quote/" + stock_symbol
        xpath_stock_name = '//div[@id="layout-col1"]/div/div/div/div/h1'
        xpath_stock_price = '//div[@id="layout-col1"]/div/div/div/div[2]/div[1]/div/span[1]'
        response = requests.get(url)
        stock_name = cls.get_response_xpath(response, xpath_stock_name)
        print(stock_name)
        stock_price = cls.get_response_xpath(response, xpath_stock_price)
        if stock_name and stock_price:
            result = f'{stock_name} - {stock_symbol}\n{stock_price}'
            return result
    
    @staticmethod
    def get_response_xpath(response, xpath_element):
        if response.status_code == 200:
            # 使用 lxml 的 etree 解析 HTML 內容
            html = response.content
            tree = etree.HTML(html)

            # 使用 XPath 選取目標元素
            result_element = tree.xpath(xpath_element)[0]
            result = result_element.text.strip()
            return result