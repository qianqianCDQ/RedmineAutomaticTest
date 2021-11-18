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
class TestNewBug():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问登录页
        self.driver.get(url_1)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)
        self.driver.get(url_2)

    def test_new_bug(self):
        # 点击新建缺陷按钮
        bug_list_page.BugListOper(self.driver).click_new_bug_btn()
        new_bug_page.NewBugScenario(self.driver).newbug(bug_subject)
        # 新建缺陷成功后的提示信息
        assert '已创建' in self.driver.page_source

    def teardown(self):
        self.driver.refresh()
        bug_details_page.BugDetailsScenario(self.driver).del_bug()
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_003_new_bug.py', '--alluredir', './report/'])