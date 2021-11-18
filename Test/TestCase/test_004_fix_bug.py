from selenium import webdriver
import time, pytest
from Test.PageObject import login_page, bug_list_page, new_bug_page, bug_details_page
from Common.parse_yml import parse_yml

# 解析host
host = parse_yml("../../Config/redmine.yml", "websites", "host")
# 登录url
url_1 = "http://"+host+"/redmine/login"
# 缺陷列表url
url_2 = "http://"+host+"/redmine/projects/project_001/issues"
# 通过时间戳，构造唯一bug subject
bug_subject = 'bug_{}'.format(time.time())
# 登录的用户名、密码
username = parse_yml("../../Config/redmine.yml", "logininfo", "username")
password = parse_yml("../../Config/redmine.yml", "logininfo", "password")


@pytest.mark.L1
class TestFixBug():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问登录页
        self.driver.get(url_1)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)
        self.driver.get(url_2)
        bug_list_page.BugListOper(self.driver).click_new_bug_btn()
        new_bug_page.NewBugScenario(self.driver).newbug(bug_subject)
        # 新建完bug，要返回到bug列表页面
        self.driver.get(url_2)

    def test_fix_bug(self):
        # 先筛选之前创建的缺陷
        bug_list_page.BugListScenario(self.driver).filter_subject(bug_subject)
        # 点击第一条缺陷（筛选出来那条）
        bug_list_page.BugListOper(self.driver).click_first_bug()
        # 将bug状态变为已关闭
        bug_details_page.BugDetailsScenario(self.driver).fix_bug()
        # 更新成功后的提示信息
        assert '更新成功' in self.driver.page_source

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-s', 'test_004_fix_bug.py', '--alluredir', './report/'])