import unittest

discover = unittest.defaultTestLoader.discover('./', pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)