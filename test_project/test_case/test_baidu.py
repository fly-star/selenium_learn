from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os


def setUpModule():
    print('test module %s start >>>>>>>>>>>' % __name__)


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test class %s start >>>>>>>>' % cls.__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidus(self):
        '''搜索关键字: HTMLTestRunner'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        # self.assertEqual(title, "unitttest_百度搜索")

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print('test class %s end >>>>>>>>>>>>>' % cls.__name__)


def tearDownModule():
    print('test module %s end >>>>>>>>>>>>>' % __name__)

if __name__ == '__main__':
    unittest.main()
