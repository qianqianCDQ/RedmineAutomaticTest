from selenium.webdriver import ActionChains
from Base.base import Base


# 页面元素对象层
class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_username(self):
        ele = Base(self.driver).get_element('name,username')
        return ele

    def find_password(self):
        ele = Base(self.driver).get_element('id,password')
        return ele

    def find_login_btn(self):
        ele = Base(self.driver).get_element('id,login-submit')
        return ele

    def find_login_name(self):
        ele = Base(self.driver).get_element('id,loggedas')
        return ele

    def find_login_failed_info(self):
        ele = Base(self.driver).get_element('id,flash_error')
        return ele


# 页面元素操作层
class LoginOper(object):

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.driver = driver

    def input_username(self, username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        ele = self.login_page.find_login_btn()
        ActionChains(self.driver).double_click(ele).perform()

    def get_login_name(self):
        return self.login_page.find_login_name().text

    def get_login_failed_info(self):
        # 返回登录失败后提示信息的文字
        return self.login_page.find_login_failed_info().text


class LoginScenario(object):

    def __init__(self, driver):
        self.login_oper = LoginOper(driver)

    def login(self, username, password):
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.click_login_btn()