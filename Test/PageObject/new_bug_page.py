from Base.base import Base


class NewBugPage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_bug_subject(self):
        # 查找并返回缺陷主题输入框元素
        ele = Base(self.driver).get_element('id,issue_subject')
        return ele

    def find_commit_btn(self):
        # 查找提交按钮，并返回元素
        ele = Base(self.driver).get_element('name,commit')
        return ele


# 页面元素操作层
class NewBugOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.new_bug_page = NewBugPage(driver)
        self.driver = driver

    def input_bug_subject(self, bug_subject):
        # 对缺陷主题输入框做clear和send_keys操作
        self.new_bug_page.find_bug_subject().clear()
        self.new_bug_page.find_bug_subject().send_keys(bug_subject)

    def click_commit_btn(self):
        # 点击提交按钮
        self.new_bug_page.find_commit_btn().click()


# 页面业务场景层
class NewBugScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.new_bug_oper = NewBugOper(driver)

    def newbug(self, bug_subject):
        # 定义新建bug场景，两个动作
        self.new_bug_oper.input_bug_subject(bug_subject)
        self.new_bug_oper.click_commit_btn()