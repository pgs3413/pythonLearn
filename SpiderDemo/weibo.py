# selenium模拟发微博

from selenium import webdriver
from time import sleep

browser=webdriver.Chrome(executable_path="SpiderDemo/chromedriver.exe")
browser.get("https://weibo.com/u/7366717559/home?wvr=5")
sleep(5)
login_btn=browser.find_elements_by_xpath('//div[@class="info_header"]/div/a')[1]
login_btn.click()
sleep(20)
# with open("SpiderDemo/weibo.html","w",encoding="utf-8") as f:
#     f.write(browser.page_source)
for i in range(100):
    testArea=browser.find_element_by_xpath('//textarea[@class="W_input"]')
    testArea.send_keys(f"肖战必糊{i}")
    sleep(0.1)
    btn=browser.find_element_by_xpath('//div[@class="func"]/a')
    btn.click()
    sleep(1)