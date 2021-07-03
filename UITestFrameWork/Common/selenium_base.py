#!/usr/bin/python3
# -*- coding=utf-8 -*-

from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Common.logs import Logger
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from Common.set_driver import set_driver

'''
https://www.jianshu.com/p/1531e12f8852
'''
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

my_logger = Logger('logger').get_log()


class SeleniumBase(object):
    def __init__(self, driver):
        self.driver =driver
        # self.driver=webdriver.Chrome()
        # self.driver.maximize_window()

    def get_web_driver(self):
        return self.driver

    def get_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(15)
        ## 隐性等待对整个driver的周期都起作用，所以只要设置一次即可

    # selenium 定位方法
    def locate_element(self, locate_type_name, value):
        if locate_type_name == 'id':
            locate_type = By.ID
        if locate_type_name == 'name':
            locate_type = By.NAME
        if locate_type_name == 'class_name':
            locate_type = By.CLASS_NAME
        if locate_type_name == 'tag_name':
            locate_type = By.TAG_NAME
        if locate_type_name == 'link':
            locate_type = By.LINK_TEXT
        if locate_type_name == 'css':
            locate_type = By.CSS_SELECTOR
        if locate_type_name == 'partial_link':
            locate_type = By.PARTIAL_LINK_TEXT
        if locate_type_name == 'xpath':
            locate_type = By.XPATH
        my_logger.info('[%s]元素识别成功' % value)
        element=WebDriverWait(self.driver, 5) \
            .until(lambda x: x.find_element(locate_type, value))
        return element if element else None

    # selenium 点击
    def click_element(self, locate_type, value):
        my_logger.info('[%s]元素点击成功' % value)
        self.locate_element(locate_type, value).click()

    # selenium 输入
    def input_data(self, locate_type, value, data):
        my_logger.info('{}元素输入{}成功'.format(value, data))
        self.locate_element(locate_type, value).send_keys(data)

    # 获取定位到的指定元素
    def get_text(self, locate_type, value):
        my_logger.info('[%s]元素定位成功' % value)
        return self.locate_element(locate_type, value).text

    # 获取标签属性
    def get_attr(self, locate_type, value, attr):
        my_logger.info('{}元素获取属性标签{}成功'.format(value, attr))
        return self.locate_element(locate_type, value).get_attribute(attr)

    # 页面截图
    def sc_shot(self, id):
        for filename in os.listdir(os.path.dirname(os.getcwd())):
            if filename == 'picture':
                break
        else:
            os.mkdir(os.path.dirname(os.getcwd()) + '/picture/')

        photo = self.driver.get_screenshot_as_file(project_dir + '/picture/'
                                                   + str(id) + str('_') + time.strftime("%Y-%m-%d-%H-%M-%S") + '.png')
        return photo

    def execute_script(self, script):
        self.driver.execute_script(script)

    def quit(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()
        my_logger.info('chrome driver closed')
