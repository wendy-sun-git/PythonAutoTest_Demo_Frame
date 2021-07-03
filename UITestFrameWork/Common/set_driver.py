from selenium import webdriver


def set_driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    return driver


if __name__ == '__main__':
    set_driver()
