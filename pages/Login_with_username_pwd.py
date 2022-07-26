from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.loginLocator import *


class LoginPage1:
    def __init__(self, driver):
        self.driver = driver

    def click_button_next_banner(self):
        print('Click button next banner')
        click_button_next_banner = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_next_banner_id())))
        click_button_next_banner.click()

    def click_button_complete_banner(self):
        print('Click button complete banner')
        click_button_complete_banner = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_complete_id())))
        click_button_complete_banner.click()

    def click_button_locate_accept(self):
        print('Click button accept locate')
        click_button_locate_accept = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_accept_locate_id())))
        click_button_locate_accept.click()

    def click_button_locate_unaccept(self):
        print('Click button unaccept locate')
        click_button_locate_unaccept = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_unaccept_locate_id())))
        click_button_locate_unaccept.click()

    def click_button_usr(self):
        print('Click username')
        click_button_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_input_usr_id())))
        click_button_usr.click()

    def enter_button_usr(self, usr):
        print('Enter username')
        enter_button_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_input_usr_id())))
        enter_button_usr.clear()
        enter_button_usr.send_keys(usr)

    def click_button_pwd(self):
        print('Click password')
        click_button_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_input_pwd_id())))
        click_button_pwd.click()

    def enter_button_pwd(self, pwd):
        print('Enter password')
        enter_button_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_input_pwd_id())))
        enter_button_pwd.clear()
        enter_button_pwd.send_keys(pwd)

    def click_button_login(self):
        print('Click button login')
        click_button_login = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((MobileBy.ID,get_button_login_id())))
        click_button_login.click()

    def click_button_enter_login(self):
        print('Click button enter login')
        click_button_enter_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_enter_login_id())))
        click_button_enter_login.click()

    def click_logo_account(self):
        print('Click logo account')
        click_logo_account = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_logo_account_id())))
        click_logo_account.click()

    def get_text_username_account(self):
        print('Get text username accoutn')
        get_text_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_text_username_account_id()))).text
        return get_text_usr

    def get_text_warning(self):
        print('Get text warning')
        get_text_warning = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_text_warning_id()))).text
        return get_text_warning

    def click_logo_okxe(self):
        print('Click logo okxe')
        click_logo = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_logo_okexe_id())))
        click_logo.click()