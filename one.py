from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

driver.find_element_by_id('translateContent').send_keys('hello')
driver.find_element_by_tag_name('button').submit()

driver.quit()