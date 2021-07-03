from PageObject.loginpage import LoginPage
from Common.selenium_base import my_logger
import time


def login(driver, username, password):
    """
    登录业务
    :param driver:浏览器驱动
    :param username:用户名
    :param password:密码
    :return:None
    """
    my_logger.info(f"使用用户名:{username},密码:{password}进行登陆")
    login_page = LoginPage(driver)
    login_page.send_username(username)
    login_page.send_password(password)
    login_page.submit()
    time.sleep(2)