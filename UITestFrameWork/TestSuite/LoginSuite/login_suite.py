import unittest

from TestCase.test_logincase import TestLogin


def return_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    print('11')
    # 自动加载：把所有测试用例加载到TestSuite里面，loadTestsFromTestCase调用测试用例类
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    print('22')
    return suite
