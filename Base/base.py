from selenium.webdriver.support.ui import WebDriverWait


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def split_locator(self, locator):
        if len(locator.split(',')) == 3:
            by = locator.split(',')[0]
            value = locator.split(',')[1] + ',' + locator.split(',')[2]
        else:
            by = locator.split(',')[0]
            value = locator.split(',')[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("Locator Err!'id',only 'name','class','tag','link','plink','xpath','css' can be used.")
        return locator_dict[by], value

    def get_element(self, locator, sec = 20):
        by, value = self.split_locator(locator)
        try:
            ele = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value))
            return ele
        except Exception as e:
            raise e

    def get_elements(self, locator, sec = 20):
        by, value = self.split_locator(locator)
        try:
            ele = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_elements(by=by, value=value))
            return ele
        except Exception as e:
            raise e


if __name__ == "__main__":
    from selenium import webdriver
    from time import sleep

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    a = "id, kw"
    bp = Base(driver)
    bp.get_element(a).send_keys("11111")
    sleep(3)
    driver.quit()