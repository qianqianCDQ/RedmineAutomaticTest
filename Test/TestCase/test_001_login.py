from selenium import webdriver
import pytest
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml


host = parse_yml("../../Config/redmine.yml", "websites", "host")
url = "http://"+host+"/redmine/login"
data = parse_csv("../../Data/test_01_login.csv")


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def teardown_class(self):
        self.driver.quit()

    def test_001_login(self, username, password, status):
        login_page.LoginScenario(self.driver).login(username, password)
        if status == '0':
            text = login_page.LoginOper(self.driver).get_login_failed_info()
            assert text == '无效的用户名或密码'
        elif status == '1':
            text = login_page.LoginOper(self.driver).get_login_name()
            assert username in text
            assert "我的工作台" in self.driver.page_source
        else:
            print('参数化的状态只能传入0或1')


if __name__ == '__main__':
    pytest.main(['-s', 'test_001_login.py', '--alluredir', './report/'])