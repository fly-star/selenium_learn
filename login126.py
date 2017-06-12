from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.126.com')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面url
url = driver.current_url
print(url)

#切换表单
driver.switch_to.frame('x-URS-iframe')
#执行登录
driver.find_element_by_css_selector("[data-placeholder='邮箱帐号或手机号']").clear()
driver.find_element_by_css_selector("[data-placeholder='邮箱帐号或手机号']").send_keys('username')
driver.find_element_by_css_selector("[data-placeholder='密码']").clear()
driver.find_element_by_css_selector("[data-placeholder='密码']").send_keys('password')
driver.find_element_by_id('dologin').click()

#返回上一级表单
driver.switch_to.parent_frame()
#返回最外层表单
driver.switch_to.default_content()