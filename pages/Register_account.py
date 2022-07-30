from locators.register import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login import *
from appium.webdriver.common.mobileby import MobileBy

class RegisterAccount:
    def __init__(self, driver):
        self.driver = driver

    def click_button_register(self):
        print("Click button register")
        click_button_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_register_id())))
        click_button_register.click()

    def enter_username_register(self, username):
        print("Click button register")
        enter_button_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, get_username_xpath())))
        enter_button_register.send_keys(username)

    def enter_pwd_register(self, pwd):
        print("Enter password register")
        enter_pwd_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, get_pwd_xpath())))
        enter_pwd_register.send_keys(pwd)

    def enter_pwd_confirm_register(self, pwd):
        print("Enter password confirm register")
        enter_pwd_cf_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, get_pwd_confirm_xpath())))
        enter_pwd_cf_register.send_keys(pwd)

    def click_button_enter_register(self):
        print("Click button enter register")
        click_button_enter_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_enter_register_id())))
        click_button_enter_register.click()

    def click_button_verify_numberphone(self):
        print("Click button verify number phone")
        click_button_verify_nbf  = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_verify_numberphone_id())))
        click_button_verify_nbf .click()
