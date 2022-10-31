# coding:utf-8
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logutils import logger


class BasePage:
    # 初始化函数
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 等待元素显示
    # location 是一个元组(By.ID, id)
    def wait_element_visible(self, location, description, wait_time=30, frequency=0.2):
        try:
            logger.info("等待元素显示：" + description)
            WebDriverWait(self.driver, wait_time, frequency).until(EC.visibility_of_element_located(location))
        except Exception:
            logger.error("元素显示失败：" + description)
            self.save_img(description)
            raise

    # 截图
    def save_img(self, description):
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "imgs")
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        img_path = os.path.join(dir_path, now+description + '.png')
        print(img_path)
        try:
            self.driver.save_screenshot(img_path)
        except Exception:
            logger.error("截图失败：" + description)
            raise

    # 获取元素
    def get_element(self, location, description):
        try:
            logger.info("获取元素：" + description)
            element = self.driver.find_element(*location)
        except Exception:
            logger.error("获取元素失败：" + description)
            self.save_img(description)
            raise
        else:
            return element

    # 点击元素
    def click_element(self, location, description, wait_time=20, frequency=0.2):
        self.wait_element_visible(location, description, wait_time, frequency)
        ele = self.get_element(location, description)
        try:
            logger.info("点击元素：" + description)
            ele.click()
        except Exception:
            logger.error("点击元素失败：" + description)
            self.save_img(description)
            raise

    # 在元素中输入文本
    def input_text(self, location, value, description, wait_time=20, frequency=0.2):
        self.wait_element_visible(location, description, wait_time, frequency)
        ele = self.get_element(location, description)
        try:
            logger.info("在元素中输入文本：" + description)
            ele.send_keys(value)
        except Exception:
            logger.error("在元素中输入文本失败：" + description)
            self.save_img(description)
            raise

    # 清空输入框文本
    def clear_text(self, location, description, wait_time=20, frequency=0.2):
        ele = self.get_element(location, description)
        try:
            logger.info("清空输入框文本：" + description)
            ele.clear()
        except Exception:
            logger.error("输入框清空文本失败：" + description)
            self.save_img(description)
            raise

