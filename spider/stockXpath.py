import requests
from lxml import etree

class stock ():
    @classmethod 
    def response_get_xpath(cls, response, xpath_element):
        if response.status_code == 200:
            # 使用 lxml 的 etree 解析 HTML 內容
            html = response.content
            tree = etree.HTML(html)

            # 使用 XPath 選取目標元素
            result_element = tree.xpath(xpath_element)[0]
            result = result_element.text.strip()
            return result



# SEARCH_TEXT = '0050'

# url = "https://tw.stock.yahoo.com/quote/" + SEARCH_TEXT

# xpath_stock_name = '//div[@id="layout-col1"]/div/div/div/div/h1'
# xpath_stock_price = '//div[@id="layout-col1"]/div/div/div/div[2]/div[1]/div/span[1]'

# # 發送 GET 請求，獲取網頁內容
# response = requests.get(url)

# # 檢查請求是否成功
# if response.status_code == 200:
#     # 使用 lxml 的 etree 解析 HTML 內容
#     html = response.content
#     tree = etree.HTML(html)

#     # 使用 XPath 選取目標元素
#     name_element = tree.xpath(xpath_stock_name)[0]
#     price_element = tree.xpath(xpath_stock_price)[0]

#     # 提取元素的文本內容
#     price = price_element.text.strip()
#     name = name_element.text.strip()

#     # 輸出結果
#     print(f"股票名稱：{name}")
#     print(f"股票價格：{price}")
# else:
#     print("網頁請求失敗")