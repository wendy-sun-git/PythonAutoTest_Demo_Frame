import unittest

from TestCase.test_query_lianjia import TestLogin


def return_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    # 自动加载：把所有测试用例加载到TestSuite里面，loadTestsFromTestCase调用测试用例类
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))

    return suite
