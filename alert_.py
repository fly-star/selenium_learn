from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#鼠标悬停至‘设置’链接
move = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(move).perform()

# b = driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div[3]/a[8]')
# print(b)

time.sleep(2)
# a = driver.execute_script("document.querySelector('.bdpfmenu').style.displayed='block';")
# print(a)

#打开搜索设置
# driver.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
js = "document.querySelector('a.setpref').click();"
print(js)
driver.execute_script(js)

#保存设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

#接受警告框
driver.switch_to_alert().accept()

driver.quit()