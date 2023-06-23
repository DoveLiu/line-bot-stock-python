from SeleniumIntergrate import SeleniumIntergrate

url = 'https://store.line.me/stickershop/product/10209090/zh-Hant'
xpath_stickers = '//section/div/div/div/div/ul/li'

driver = SeleniumIntergrate.get_driver_url(url)
stickers = SeleniumIntergrate.find_elements_by_xpath(driver, xpath_stickers)

for i in range(len(stickers)):
    sticker = SeleniumIntergrate.find_element_by_xpath(driver, f'{xpath_stickers}[{i + 1}]')
    if sticker:
        print(f'sticker: {sticker.text}')


SeleniumIntergrate.quit(driver)