from selenium import webdriver
import unittest
import time


def setUpModule():
    print('test module %s start >>>>>>>>>>>'%__name__)


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('test class %s start >>>>>>>>'%cls.__name__)

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.youdao.com'

    @unittest.skip
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('query').clear()
        driver.find_element_by_id('query').send_keys('webdriver')
        driver.find_element_by_id('qb').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "webdriver - 有道搜索")

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print('test class %s end >>>>>>>>>>>>>'%cls.__name__)


def tearDownModule():
    print('test module %s end >>>>>>>>>>>>>'%__name__)

if __name__ == '__main__':
    unittest.main()