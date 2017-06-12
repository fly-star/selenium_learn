from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#获取输入框尺寸
size = driver.find_element_by_id('kw').size
print(size)

#返回百度页面底部备案信息
text = driver.find_element_by_id('cp').text
print(text)

#返回元素的属性值，可以是id,name,type或其他任意属性
attr = driver.find_element_by_id('kw').get_attribute('type')
print(attr)

#返回元素的结果是否可以见，返回结果为TRue或False
result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()
