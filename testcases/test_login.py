# coding:utf-8
from selenium import webdriver
from po.loginpage import LoginPage
from po.mainpage import MainPage
from testdata import common_data as c_data
from testdata import login_data as l_data
from utils.logutils import logger
import pytest
import sys


class TestLogin:
    def setup(self):
        # self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver = webdriver.Chrome()
        self.driver.get(c_data.home_url)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('username, password', l_data.success_data)
    def test_login_success(self, username, password):
        page = LoginPage(self.driver)
        try:
            page.login(username, password)
            # assertion
            page.wait_element_visible(MainPage.MenuText, "登录后置-主页面系统名", 50)
            ele_text = page.get_element(MainPage.MenuText, "登录后置-主页面系统名").text
            exp_text = "PESCMS Team"
            assert ele_text == exp_text
        except AssertionError:
            logger.error(sys._getframe().f_code.co_name + "用例失败原因：" + "断言失败")
            return
        except Exception:
            logger.error(sys._getframe().f_code.co_name + "用例失败原因：" + "步骤中间结果异常")
            assert 0


if __name__ == '__main__':
    pytest.main(['-v', 'test_login.py'])
