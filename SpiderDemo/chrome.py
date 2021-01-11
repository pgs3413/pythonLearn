# selenium

from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象
browser=webdriver.Chrome(executable_path="SpiderDemo/chromedriver.exe")

# 浏览器自动化操作

# 让浏览器发起一个指定url对应请求
# browser.get("http://scxk.nmpa.gov.cn:81/xk/")

# 获取浏览器当前页面的页面源码数据
# page_text=browser.page_source

# tree=etree.HTML(page_text)
# li_list=tree.xpath('//ul[@id="gzlist"]/li')
# for li in li_list:
#     name=li.xpath('./dl/@title')[0]
#     print(name)
# browser.quit()

# 淘宝操作
# browser.get("https://www.taobao.com/")

# 标签定位
# search=browser.find_element_by_id('q')
# 标签交互
# search.send_keys('iphone')

# 执行一组js代码
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# sleep(5)

# 点击按钮
# btn=browser.find_element_by_css_selector('.btn-search')
# btn.click()

# browser.get('https://www.baidu.com')
# sleep(2)

# browser.back()
# sleep(2)
# browser.forward()

# sleep(5)
# browser.quit()

browser.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

# 标签存在于iframe标签中
browser.switch_to.frame("iframeResult") #id 切换浏览器标签定位的作用域

div=browser.find_element_by_id("draggable")

# 拖动标签
# 动作链 （触发一系列的动作）
from selenium.webdriver import ActionChains

# 实例化一个动作链对象
actionChains=ActionChains(browser)

actionChains.click_and_hold(div)
# actionChains.move_by_offset(30,30)

for i in range(5):
    actionChains.move_by_offset(17,0).perform()
    sleep(0.3)

# 立即执行动作链操作
# actionChains.perform()



# 释放动作链
actionChains.release()
