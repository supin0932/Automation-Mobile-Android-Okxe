from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_icon_account(self):
        print("Click icon account")
        click_icon_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_logo_account_id())))
        click_icon_account.click()

    def click_icon_setting(self):
        print("Click icon setting")
        click_icon_setting = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/iv_profile")))
        click_icon_setting.click()

    def click_button_logout(self):
        print("Click button logout")
        click_button_logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_logout_id())))
        click_button_logout.click()

    def click_button_confirm_logout(self):
        print("Click button confirm logout")
        click_button_confirm_logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_confirm_logout_id())))
        click_button_confirm_logout.click()

