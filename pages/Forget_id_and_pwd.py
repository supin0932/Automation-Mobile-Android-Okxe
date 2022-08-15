from locators.forget_pwd import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login import *
from appium.webdriver.common.mobileby import MobileBy

class ForgetPassword:
    def __init__(self, driver):
        self.driver = driver

    def click_button_forget_pwd(self):
        print("Click forget password")
        click_button_fg_pwd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MobileBy.ID,get_button_forget_pwd_id())))
        click_button_fg_pwd.click()

    def enter_numberphone(self, numberphone):
        print("Enter numberphone")
        enter_numberphone = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.ID, get_enter_numberphone_id())))
        enter_numberphone.send_keys(numberphone)

    def enter_otp(self, n1, n2, n3, n4, n5, n6):
        print("Enter opt")
        enter_n1 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu1_otp_xpath())))
        enter_n1.send_keys(n1)
        enter_n2 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu2_otp_xpath())))
        enter_n2.send_keys(n2)
        enter_n3 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu3_otp_xpath())))
        enter_n3.send_keys(n3)
        enter_n4 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu4_otp_xpath())))
        enter_n4.send_keys(n4)
        enter_n5 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu5_otp_xpath())))
        enter_n5.send_keys(n5)
        enter_n6 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.XPATH, get_nu6_otp_xpath())))
        enter_n6.send_keys(n6)

    def click_button_continue(self):
        print("Click button continue")
        click_button_continue = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((MobileBy.ID, get_button_continue_id())))
        click_button_continue.click()


    def click_tab_username(self):
        print("Click tab username")
        click_tab_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_tab_usrname_accesid())))
        click_tab_usr.click()

    def get_username(self):
        print("Get username")
        get_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_usrname_in_tab_id()))).text
        return get_usr

    def click_tab_pwd(self):
        print("Click tab password")
        click_tab_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_tab_pwd_accesid())))
        click_tab_pwd.click()

    def enter_pwd(self, pwd):
        print("Enter password")
        enter_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_enter_new_pwd_id())))
        enter_pwd.send_keys(pwd)

    def enter_pwd_confirm(self, pwdcf):
        print("Enter password confirm")
        enter_pwd_confirm = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_enter_new_pwd_confirm_id())))
        enter_pwd_confirm.send_keys(pwdcf)

    def click_button_comback_login(self):
        print("Click button comback login")
        click_bt_cb_lg = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_comback_login_id())))
        click_bt_cb_lg.click()

    def click_button_update_pwd(self):
        print("Click button update password")
        click_bt_up_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_update_pwd_id())))
        click_bt_up_pwd.click()

    def get_text_warning(self):
        print('Get text warning')
        get_text_warning = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_text_warning_otp_id())))
        text = get_text_warning.text
        return text

    def click_button_back(self):
        print("Click button back")
        click_bt_back = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, get_bt_back())))
        click_bt_back.click()

    def click_button_close(self):
        print("Click button close")
        click_bt_close = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, get_bt_close())))
        click_bt_close.click()
