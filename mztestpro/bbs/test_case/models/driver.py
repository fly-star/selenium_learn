from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as Remote


#启动浏览器驱动
def browser():
    # host = '127.0.0.1:4444'
    # dc = {"browserName": "firefox"}
    # driver = Remote(command_executor='http://' + host + '/wd/hub',
    #                           desired_capabilities=dc)
    driver = webdriver.Firefox()
    return driver



if __name__ == '__main__':
    driver = browser()
    driver.get('http://www.baidu.com')
    driver.quit()

