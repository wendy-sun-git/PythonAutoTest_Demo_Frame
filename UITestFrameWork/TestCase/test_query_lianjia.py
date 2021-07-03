#!/usr/bin/python3
# -*- coding=utf-8 -*-
import unittest

from selenium import webdriver
from pyquery import PyQuery as pq
from ddt import  ddt ,unpack, file_data, data
import time
import pymysql
from Common.logs import Logger
from Common.selenium_base import SeleniumBase

url = 'https://sz.fang.lianjia.com/loupan/bba0eba300/'


@ddt
class QueryLianjia(unittest.TestCase):

    def setUp(self):
        self.driver = SeleniumBase().get_web_driver()
        self.log = Logger().get_log()
        self.url = url
        self.se = SeleniumBase(self.driver)

    def tearDown(self):
        SeleniumBase(self.driver).quit()

    def Start(self):

        # 这里我用到jQuery scrollTop() 在这里也是适用的，用來操作滚动条
        a = "window.scrollTo(0,800);"
        b = "window.scrollTo(0,1600);"
        c = "window.scrollTo(0,3200);"

        # 我这里没有获取页数，直接用range()遍历了！
        # 提示：最好还是获取总页数，以免抓取的数据遗漏
        for i in range(20):
            self.log.info('开始你的表演...')
            # 这块我们先找到class="resblock-list-wrapper"，并且判断该class是否存在
            # 因为很多时候网络的问题导致一些资源没有加载完成，就会报错
            self.se.open_url(self.url)

            label = self.se.locate_element('class_name', 'resblock-list-wrapper')
            if len(label) != 0:
                self.log.info('正在解析网页请稍等.....')
                # 调用Traversal()方法
                # self.Traversal()
                time.sleep(3)
                self.log.info('数据保存完成-正在跳转到下一页....')
                next_page = self.se.locate_element('class_name', 'next')
                next_page.click()
                self.se.execute_script(a)
                time.sleep(3)
                # 滑动第2次
                self.se.execute_script(b)
                time.sleep(3)
                # 滑动第3次
                self.se.execute_script(c)
                time.sleep(7)
                # self.Traversal()

        # 如果找不到元素则关闭浏览器
        else:
            print('网页加载异常(5秒后自动关闭浏览器)')
            time.sleep(5)
            self.se.close()

    def Traversal(self):
        # 解析网页
        html = self.se.page_source
        # 我用到pyquery解析器，并且遍历 li 标签，其实都差不多，这个解析器对css选择比较友好，个人感觉
        # 当然我感觉得没用，还有一些大神也是这样觉得滴
        doc = pq(html)
        house = doc('.resblock-list-wrapper li').items()
        # 直接遍历，开始骚操作，提取自己需要的信息
        for i in house:
            house_data = {
                '小区': i.find('.name').text(),
                '房类': i.find('.resblock-type').text(),
                '售卖状态': i.find('.sale-status').text(),
                '地址': i.find('.resblock-location').text(),
                '内室种类': i.find('.resblock-room').text(),
                '面积': i.find('.resblock-area').text(),
                '顾问': i.find('.agent').text().strip('新房顾问：'),
                '房价': i.find('.number').text(),
                '总价': i.find('.second').text(),
                '链接': i.find('.resblock-img-wrapper').attr('href')
            }
            self.log.info(house_data)
            # 当然抓取到的数据我保存到mysql数据库中，改数据库我已经提前建好了表格了的。
            # 开始数据库 本地地址(你也可以存到其他数据库中)、用户名、密码、端口、数据库名称
            db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='lianjie')

            # 声明游标
            cursor = db.cursor()
            # 基本的sql插入語句
            sql = "insert into lianjie_data(Community,Category,Status,Address,Chamber,Area,Adviser,Unit_price,Total_price," \
                  "Url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (
                house_data["小区"], house_data["房类"], house_data["售卖状态"], house_data["地址"], house_data["内室种类"],
                house_data["面积"],
                house_data["顾问"], house_data["房价"], house_data["总价"], house_data["链接"])
            # 执行语句
            cursor.execute(sql, params)
            # 这里一定要用到commit()提交 不然完成不了信息的保存
            db.commit()
            # 关闭数据库
            db.close()
            time.sleep(2)


if __name__ == '__main__':
    qlj = QueryLianjia()
    qlj.Start()


class TestLogin:
    pass