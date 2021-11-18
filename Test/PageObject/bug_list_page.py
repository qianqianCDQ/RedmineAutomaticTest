from Base.base import Base
from selenium.webdriver.support.select import Select


class BugListPage(object):

    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_new_bug_btn(self):
        # 查找并返回新建缺陷元素
        ele = Base(self.driver).get_element('xpath,//*[@id="content"]/div[1]/a')
        return ele

    def find_filter_select(self):
        # 增加过滤器的下拉列表
        ele = Base(self.driver).get_element('id,add_filter_select')
        return ele

    def find_values_subject(self):
        # 输入主题的框
        ele = Base(self.driver).get_element('id,values_subject')
        return ele

    def find_checked_btn(self):
        # 应用按钮
        ele = Base(self.driver).get_element('xpath,//*[@id="query_form_with_buttons"]/p/a[1]')
        return ele

    def find_first_bug(self):
        # 找到第一条缺陷
        ele = Base(self.driver).get_element("xpath,//*[starts-with(@id,'issue')]/td[6]/a")
        return ele


# 页面元素操作层
class BugListOper(object):

    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.bug_list_page = BugListPage(driver)
        self.driver = driver

    def click_new_bug_btn(self):
        # 点击新建缺陷
        self.bug_list_page.find_new_bug_btn().click()

    def select_filter_select(self, visible_text):
        # 按visible_text，增加过滤器
        ele = self.bug_list_page.find_filter_select()
        Select(ele).select_by_visible_text(visible_text)

    def input_values_subject(self, subject):
        # 输入要过滤的主题
        self.bug_list_page.find_values_subject().send_keys(subject)

    def click_checked_btn(self):
        # 点击应用按钮
        self.bug_list_page.find_checked_btn().click()

    def click_first_bug(self):
        # 点击第一条缺陷
        self.bug_list_page.find_first_bug().click()


# 页面业务场景层
class BugListScenario(object):

    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.bug_list_oper = BugListOper(driver)

    def add_filter(self, visible_text):
        # 定义一个场景，增加过滤器
        self.bug_list_oper.select_filter_select(visible_text)

    def filter_subject(self, subject):
        # 定义一个场景，按主题筛选
        self.bug_list_oper.select_filter_select('主题')
        self.bug_list_oper.input_values_subject(subject)
        self.bug_list_oper.click_checked_btn()