from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from spider.SeleniumIntergrate import SeleniumIntergrate

"""
selenium 爬蟲
太慢了，先棄用
"""
class YahooStock():
    def __init__():
        pass

    @classmethod    
    def get_stock_info(cls, stock_symbol):
        url = 'https://tw.stock.yahoo.com/quote/'
        xpath_stock_name = '//div[@id="layout-col1"]/div/div/div/div/h1'
        xpath_stock_price = '//div[@id="layout-col1"]/div/div/div/div[2]/div[1]/div/span[1]'

        driver = SeleniumIntergrate.get_driver_url(url + stock_symbol)
        stock_name = SeleniumIntergrate.find_element_by_xpath(driver, xpath_stock_name).text
        stock_price = SeleniumIntergrate.find_element_by_xpath(driver, xpath_stock_price).text
        stock_symbol = SEARCH_TEXT
        result = f'{stock_name} - {stock_symbol}\n{stock_price}'
        SeleniumIntergrate.quit(driver)
        return result

# 股票代號
SEARCH_TEXT = '0050'

# yahoo 股市首頁
# url = 'https://tw.stock.yahoo.com/'
# 用這個 + 股票代號就可以搜尋
url = 'https://tw.stock.yahoo.com/quote/'

xpath_stock_name = '//div[@id="layout-col1"]/div/div/div/div/h1'
xpath_stock_price = '//div[@id="layout-col1"]/div/div/div/div[2]/div[1]/div/span[1]'

# options = Options()

# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# driver_path = ChromeDriverManager().install()
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# driver.get(url)

# def find_element_by_xpath(xpath_string:str):
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_string)))
#     return element

# def find_elements_by_xpath(xpath_string:str):
#     elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath_string)))
#     return elements

# stock_name = find_element_by_xpath(xpath_stock_name).text
# stock_price = find_element_by_xpath(xpath_stock_price).text
# stock_symbol = SEARCH_TEXT

# print(f'{stock_name} - {stock_symbol}\n{stock_price}')

# input()
# driver.quit() 

# driver = SeleniumIntergrate.get_driver_url(url)
# stock_name = SeleniumIntergrate.find_element_by_xpath(driver, xpath_stock_name).text
# stock_price = SeleniumIntergrate.find_element_by_xpath(driver, xpath_stock_price).text
# stock_symbol = SEARCH_TEXT
# print(f'{stock_name} - {stock_symbol}\n{stock_price}')
# SeleniumIntergrate.quit(driver)
