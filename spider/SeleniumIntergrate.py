from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class SeleniumIntergrate():
        
    # def __init__(self):
    #     pass

    @classmethod
    def get_driver_url(cls, url):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver_path = ChromeDriverManager().install()
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        return driver

    @classmethod
    def find_element_by_xpath(cls, driver, xpath_string:str):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_string)))
        return element
    
    @classmethod
    def find_elements_by_xpath(cls, driver, xpath_string:str):
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath_string)))
        return elements

    @classmethod
    def quit(cls, driver):
        driver.quit() 