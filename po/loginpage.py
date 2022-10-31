# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from po.basepage import BasePage


class LoginPage(BasePage):
    username_input = (By.NAME, "account")
    password_input = (By.NAME, "passwd")
    login_btn = (By.TAG_NAME, "button")
    
    # 登录
    def login(self, user, pwd):
        self.clear_text(self.username_input, "登录-用户名输入框清空")
        self.input_text(self.username_input, user, "登录-用户名输入", 10, 0.2)
        self.clear_text(self.password_input, "登录-密码输入框清空")
        self.input_text(self.password_input, pwd, "登录-密码输入", 10, 0.2)
        self.click_element(self.login_btn, "登录-登录按钮点击", 10, 0.2)