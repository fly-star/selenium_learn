import unittest
import sys
print(sys.version_info, ...)


def setUpModule():
    print('test module %s start >>>>>>>>>>>>>>>' % __name__)


def tearDownModule():
    print('test module %s end >>>>>>>>>>>>>>' % __name__)


class Count(object):

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


class Sub(object):

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def sub(self):
        return self.a - self.b


class TestCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test class start >>>>>>>>>>>>')

    @classmethod
    def tearDownClass(cls):
        print('test class end >>>>>>>>>>')

    def setUp(self):
        print('test start')

    @unittest.skip('直接跳过测试')
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    @unittest.skipIf(3 > 2, '当条件为真时跳过测试')
    def test_add2(self):
        j = Count(41, 77)
        self.assertEqual(j.add(), 118)

    def tearDown(self):
        print('test end')


class TestSub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test class %s start >>>>>>>>>>>>' % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        print('test class end >>>>>>>>>>')

    def setUp(self):
        print('test sub start')

    @unittest.skipUnless(3 > 2, '当条件为真时执行测试')
    def test_sub(self):
        j = Sub(5, 2)
        self.assertEqual(j.sub(), 3)

    @unittest.expectedFailure
    def test_sub2(self):
        j = Sub(45, 5)
        self.assertEqual(j.sub(), 40)

    def tearDown(self):
        print('test sub end')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_add'))
    # suite.addTest(TestSub())

    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()
