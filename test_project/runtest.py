import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#制定搜索目录
start_dir = r'./test_case'
discover = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern='test*.py')

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H-%M-%S")

    filename = 'report/' + now + 'result.html'

    #定义报告存放路径
    fp = open(filename, 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用力执行情况:')
    runner.run(discover)
    fp.close()