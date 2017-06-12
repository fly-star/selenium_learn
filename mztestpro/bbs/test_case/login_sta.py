from time import sleep
import unittest
import random
import sys

sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit, function
from page_obj.loginPage import Login



class loginTest(myunit.MyTest):
    '''社区登录测试'''

    # @classmethod
    # def setUpClass
    #测试用户登录
    def user_login_verify(self, username='', password=''):
        po = Login(self.driver)
        po.user_login(username, password)
        return po

    #用户名、密码为空登录测试
    def test_login_without_username_and_password(self):
        po = self.user_login_verify()
        function.insert_img(self.driver, 'user_and_pwd_empty.jpg')
        self.assertEqual(po.user_error_hint(), '账号不能为空')
        self.assertEqual(po.pwd_error_hint(), '密码不能为空')

    #用户名正确、密码为空登录测试
    def test_login_without_password(self):
        po = self.user_login_verify(username='pytest')
        function.insert_img(self.driver(), 'only_pwd_empty.jpg')
        self.assertEqual(po.pwd_error_hint(), '密码不能为空')

    #用户名为空、密码正确登录测试
    def test_login_without_username(self):
        po = self.user_login_verify(password='123456')
        function.insert_img(self.driver, 'only_user_empty.jpg')
        self.assertEqual(po.user_error_hint(), '账号不能为空')

    #用户名和密码不匹配登录测试
    def test_login_username_missmatch_password(self):
        chars = random.sample([chr(i) for i in range(64, 129)], 8)
        username = ''.join(chars)
        po = self.user_login_verify(username=username, password='123456')
        function.insert_img(self.driver, 'username_missmatch_password.jpg')
        self.assertEqual(po.pwd_error_hint(), '密码和账号不匹配')

    #用户名和密码正确登录测试
    def test_login_username_match_password(self):
        po = self.user_login_verify(username='weira@flyme.com', password='19901114yctd')
        sleep(3)
        function.insert_img(self.driver, 'username_match_password.jpg')
        self.assertEqual(po.user_login_success(), 'weira')


if __name__ == '__main__':
    unittest.main()
