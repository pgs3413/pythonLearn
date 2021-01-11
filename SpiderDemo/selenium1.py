# 模拟登录qq空间

from selenium import webdriver
from time import sleep

browser=webdriver.Chrome(executable_path="SpiderDemo/chromedriver.exe")
browser.get("https://qzone.qq.com/")
browser.switch_to.frame("login_frame")
a_tag=browser.find_element_by_id("switcher_plogin")
a_tag.click()
u_tag=browser.find_element_by_id("u")
p_tag=browser.find_element_by_id("p")
login_tag=browser.find_element_by_id("login_button")
u_tag.send_keys("2113114379")
sleep(1)
p_tag.send_keys("pgs990525")
sleep(1)
login_tag.click()
