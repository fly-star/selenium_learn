from selenium import webdriver
#引入keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id('kw').send_keys('seleniumm')

#删除多输入的一个m
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

#输入空格加教程
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')


#ctrl+a全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

#ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

#ctrl+v粘贴内容到输入框
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')

#通过回车键来代替单击操作
driver.find_element_by_id('kw').send_keys(Keys.ENTER)