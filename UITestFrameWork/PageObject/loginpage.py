#!/usr/bin/python3
# -*- coding=utf-8 -*-

from selenium.webdriver.common.by import By
from Common.selenium_base import SeleniumBase, my_logger
from Common.BaseGetExcel import BaseGetExcel
from Common.set_driver import set_driver


class LoginPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def send_username(self, username):
        my_logger.info(f"输入用户名{username}")
        self.input_data(By.ID, "TANGRAM__PSP_11__userName", username)

    def send_password(self, password):
        my_logger.info(f"输入密码{password}")
        self.input_data(By.ID, "TANGRAM__PSP_11__password", password)

    def submit(self):
        my_logger.info("点击登录按钮")
        self.click_element(By.ID, "TANGRAM__PSP_11__submit")


if __name__ == "__main__":
    driver1 = set_driver()
    se = SeleniumBase(driver1).get_url('https://www.baidu.com')
    lg = LoginPage(driver1)
    lg.send_username('aaaa')
    # lg.send_password('bbbb')
    # lg.submit()
