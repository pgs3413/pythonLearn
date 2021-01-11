# 无头浏览器+反检测


# 无可视化界面
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

browser=webdriver.Chrome(executable_path="SpiderDemo/chromedriver.exe",chrome_options=chrome_options)

browser.get("https://www.baidu.com")
# print(browser.page_source)
browser.quit()


# 规避检测
from selenium.webdriver import ChromeOptions

options=ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-automation'])
browser=webdriver.Chrome(executable_path="SpiderDemo/chromedriver.exe",chrome_options=chrome_options,options=options)