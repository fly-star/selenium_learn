from selenium import webdriver
from time import sleep

#访问百度
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#设置浏览器大小
driver.set_window_size(600, 600)

#搜索
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').submit()
sleep(2)

#调用JS执行代码
js = 'window.scrollTo(100, 450);'
driver.execute_script(js)
sleep(3)

driver.quit()