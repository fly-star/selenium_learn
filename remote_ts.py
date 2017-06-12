from selenium import  webdriver

#调用remote方法
# driver = webdriver.Remote(command_execute='http://127.0.0.1:4444/wd/hub')

print(webdriver.__dict__.get('Remote'))
