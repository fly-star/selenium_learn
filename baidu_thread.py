from threading import Thread
from selenium import webdriver
from time import ctime, sleep


def test_baidu(browser, search):
    print('% start, %s'%(browser,ctime()))
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()
    print('%s end, %s'%(browser, ctime()))


if __name__ == '__main__':
    lists = {'chrome': 'threading',
             'firefox': 'python'
    }

    threads = []

    #创建线程
    for browser, search in lists.items():
        t = Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    #启动线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()