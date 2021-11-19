from Base.base import Base
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# bug列表页
class BugDetailsPage(object):

    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_edit_btn(self):
        # 查找并返回编辑按钮
        ele = Base(self.driver).get_element('xpath,//*[@id="content"]/div[1]/a[1]')
        return ele

    def find_status_select(self):
        # 缺陷状态下拉列表
        ele = Base(self.driver).get_element('id,issue_status_id')
        return ele

    def find_commit_btn(self):
        # 提交按钮
        ele = Base(self.driver).get_element('xpath,//*[@id="issue-form"]/input[6]')
        return ele

    def find_del_btn(self):
        # 详情页删除按钮
        ele = Base(self.driver).get_element('xpath,//*[@id="content"]/div[1]/a[5]')
        return ele


# 页面元素操作层
class BugDetailsOper(object):

    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.bug_list_page = BugDetailsPage(driver)
        self.driver = driver

    def click_edit_btn(self):
        # 点击编辑按钮
        self.bug_list_page.find_edit_btn().click()

    def select_filter_select(self, visible_text):
        # 通过visible_text，修改缺陷状态
        ele = self.bug_list_page.find_status_select()
        Select(ele).select_by_visible_text(visible_text)

    def click_commit_btn(self):
        # 点击提交按钮
        self.bug_list_page.find_commit_btn().click()

    def click_del_btn(self):
        self.bug_list_page.find_del_btn().click()


# 页面业务场景层
class BugDetailsScenario(object):

    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.bug_details_oper = BugDetailsOper(driver)
        self.driver = driver

    def fix_bug(self):
        # 定义一个场景，将缺陷置为已关闭状态
        self.bug_details_oper.click_edit_btn()
        self.bug_details_oper.select_filter_select('已关闭')
        self.bug_details_oper.click_commit_btn()

    def del_bug(self):
        self.bug_details_oper.click_del_btn()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        sleep(2)