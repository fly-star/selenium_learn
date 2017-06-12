from selenium import webdriver
from .driver import browser
import unittest
import os


class MyTest(unittest.TestCase):
    '''自定义测试框架基类'''

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()