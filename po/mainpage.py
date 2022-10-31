from selenium import webdriver
from selenium.webdriver.common.by import By
from po.basepage import BasePage


class MainPage(BasePage):
    MenuText = (By.XPATH, "//header/h1/a[text()='PESCMS Team']")
