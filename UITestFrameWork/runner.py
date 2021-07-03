import unittest
import os
import time
import HTMLTestRunner
from TestSuite.LoginSuite import login_suite

current_path = os.getcwd()  # get current path
case_path = os.path.join(current_path, 'TestCase')  # get TestCase path
report_path = os.path.join(current_path, 'Report')  # get Report path


project_dir = os.getcwd()


class TestRunner(object):
    ''' 执行测试用例 '''

    def __init__(self, cases="../", title="WEB_UI_AUTOTEST_", description="Test case execution"):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):
        for filename in os.listdir(project_dir):
            if filename == "Report":
                break
        else:
            os.mkdir(project_dir + '/Report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        report_title = self.title + now + '.html'
        result_path = os.path.join(report_path, report_title)
        print(result_path)

        # mylogger.info('reportpath={}'.format(result_path))

        test_suite = unittest.TestSuite()
        test_suite.addTest(login_suite.return_suite())

        # unittest.TextTestRunner(verbosity=2).run(test_suite)

        with open(result_path, 'wb') as report:
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=report, title=report_title, description=self.des)
            runner.run(test_suite)


if __name__ == "__main__":
    print("start login")
    TestRunner().run()
