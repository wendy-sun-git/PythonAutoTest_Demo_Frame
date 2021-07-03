#!/usr/bin/python3
# -*- coding=utf-8 -*-
import time
import unittest
from readconf import *
from ddt import ddt, unpack, data, file_data
from Business.Base_url import UrlIndex
from Common.selenium_base import SeleniumBase, my_logger
from Business.login_business import login
from Common.set_driver import set_driver
import os


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver=set_driver()
        my_logger.info('[TestLogin]:setUp....')

    def tearDown(self):
        SeleniumBase(self.driver).quit()
        my_logger.info('[TestLogin]:teardown....')

    # user_args = read_excels_data('TestData/login_user_password.xlsx')
    # @file_data(*user_args)

    @unpack
    @file_data(os.path.join(os.getcwd(), r'TestData\json_file\login_user_password.json'))
    def test_login(self, **kwargs):
        my_logger.info('[test_login]:start')
        username=kwargs.get('username')
        password=kwargs.get('password')
        assert_type=kwargs.get('assert_type')

        se=SeleniumBase(self.driver)
        se.get_url(ReadConf.get_url('baidu_url'))
        print('url={}'.format(ReadConf.get_url('baidu_url')))
        # my_logger.info("[TestLogin]:title={},current_url={} ...".format(self.driver.title, self.driver.current_url))
        # my_logger.info("[TestLogin]:page_source={} ...".format(self.driver.page_source))

        time.sleep(1)
        # 进入登录页面
        se.locate_element('link', '登录').click()
        # self.driver.find_element_by_link_text('登录').click()
        # #选择用户名登录方式
        se.locate_element('xpath', '//*[@class="tang-pass-footerBar"]/p[text()="用户名登录"]').click()
        # self.driver.find_element_by_xpath('//*[@class="tang-pass-footerBar"]/p[text()="用户名登录"]').click()
        # 直接点击登录
        se.locate_element('class_name', "pass-form-item-submit").click()
        # self.driver.find_element_by_class_name("pass-form-item-submit").click()

        # err_str = se.locate_element('xpath','//*[@id="TANGRAM__PSP_3__error"]').text
        # # err_str=self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__error"]').text
        # try:
        #     assert err_str == '请您输入手机/邮箱/用户名'
        #     print('Test Pass')
        # except:
        #     print('Test Fail')

        login(self.driver, username, password)
        se.sc_shot('aaa')

        if assert_type == '1':
            my_logger.info("断言登陆成功---1")
            # self.driver.find_element_by_class_name('vcode-close').click()
            text =self.driver.find_element_by_class_name('quit').text
            self.assertIn("退出", "退出", '登陆成功断言')

        elif assert_type == "2":
            my_logger.error("登陆失败断言---2")
            text=self.driver.find_element_by_class_name("mod-page-tipInfo-gray1").text
            self.assertIn("安全", text, '登陆失败断言')

        elif assert_type == "3":
            my_logger.error("登陆失败断言---3")
            text=self.driver.find_element_by_class_name("mod-page-tipInfo-gray1").text
            self.assertIn("安全", text, '登陆失败断言')

        elif assert_type == "4":
            my_logger.error("登陆失败断言---4")
            text=self.driver.find_element_by_class_name("mod-page-tipInfo-gray1").text
            self.assertIn("安全", text, '登陆失败断言')

        else:
            my_logger.error(f"未知断言类型{assert_type}")
            self.assertTrue(False, "未知断言类型")
