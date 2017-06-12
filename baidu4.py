from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Firefox()
driver.get('http:www.baidu.com')

print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id('kw22')
        if el.is_displayed():
            break
    except:
        pass
        sleep(1)
else:
    print('timeout')
driver.close()
print(ctime())