from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.loginLocator import *


class LoginPage2:
    def __init__(self, driver):
        self.driver = driver

    def click_button_login(self):
        print('Click login')
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_button_login_id())))
        click_login.click()

    def click_icon_facebook(self):
        print('Click icon facebook')
        click_iconfacebook = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_icon_login_facebook_id())))
        click_iconfacebook.click()

    def click_icon_gmail(self):
        print('Click icon gmail')
        click_icongmail = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_icon_gmail_id())))
        click_icongmail.click()


    def click_username_facebook(self):
        print("Click username facebook")
        click_username_fb = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,get_usr_facebook_id())))
        click_username_fb.click()

    def click_password_facebook(self):
        print("Click password facebook")
        click_password_fb = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,get_pwd_facebook_id())))
        click_password_fb.click()

    def enter_username_facebook(self, username):
        print("Enter username facebook")
        enter_username_fb = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_usr_facebook_id())))
        enter_username_fb.clear()
        enter_username_fb.send_keys(username)

    def enter_password_facebook(self, pwd):
        print("Enter password facebook")
        enter_password_fb = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID,get_pwd_facebook_id())))
        enter_password_fb.clear()
        enter_password_fb.send_keys(pwd)


    def click_login_facebook(self):
        print("Click login facebook")
        enter_password_fb = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,get_button_login_fb_id())))
        enter_password_fb.click()


    def click_veryfi_numberphone(self):
        print("Click veryfi numberphone")
        click_veryfi_nbf = self.driver.find_element_by_css_selector(get_verify_numberphone_button_css())
        click_veryfi_nbf.click()

    def click_logout(self):
        print("Click logout")
        click_logout = self.driver.find_element_by_css_selector(get_button_logout_css())
        click_logout.click()

    def enter_numberphone(self, number):
        print("Enter numberphone")
        enter_nbf = self.driver.find_element_by_css_selector(get_numberphone_css())
        enter_nbf.clear()
        enter_nbf.send_keys(number)

    def click_continue_button(self):
        print("Click continue")
        click_continue = self.driver.find_element_by_css_selector(get_continue_button_css())
        click_continue.click()

    def enter_otp(self, n1, n2, n3, n4, n5, n6):
        print("Enter OTP")
        enter_opt6 = self.driver.find_element_by_xpath(get_number6_opt_xpath())
        enter_opt6.clear()
        enter_opt6.send_keys(n6)

        enter_opt1 = self.driver.find_element_by_xpath(get_number1_opt_xpath())
        enter_opt1.clear()
        enter_opt1.send_keys(n1)

        enter_opt2 = self.driver.find_element_by_xpath(get_number2_opt_xpath())
        enter_opt2.clear()
        enter_opt2.send_keys(n2)

        enter_opt3 = self.driver.find_element_by_xpath(get_number3_opt_xpath())
        enter_opt3.clear()
        enter_opt3.send_keys(n3)

        enter_opt4 = self.driver.find_element_by_xpath(get_number4_opt_xpath())
        enter_opt4.clear()
        enter_opt4.send_keys(n4)

        enter_opt5 = self.driver.find_element_by_xpath(get_number5_opt_xpath())
        enter_opt5.clear()
        enter_opt5.send_keys(n5)

    def click_link_facebook(self):
        print("Click link facebook")
        click_link_fb = self.driver.find_element_by_xpath(get_click_link_facebook_xpath())
        click_link_fb.click()

    def click_username_gmail(self):
        print("Click username gmail")
        click_usr_gm = self.driver.find_element_by_id(get_usr_gmail_id())
        click_usr_gm.click()

    def enter_username_gmail(self, username):
        print("Enter username gmail")
        enter_usr_gm = self.driver.find_element_by_id(get_usr_gmail_id())
        enter_usr_gm.clear()
        enter_usr_gm.send_keys(username)

    def click_password_gmail(self):
        print("Click password gmail")
        click_pwd_gm = self.driver.find_element_by_xpath(get_pwd_gmail_xpath())
        click_pwd_gm.click()

    def enter_password_gmail(self, pwd):
        print("Enter password gmail")
        enter_pwd_gm = self.driver.find_element_by_xpath(get_pwd_gmail_xpath())
        enter_pwd_gm.clear()
        enter_pwd_gm.send_keys(pwd)

    def click_continue_pwd_button(self):
        print("Click continue button")
        click_continue_button = self.driver.find_element_by_css_selector(get_continue_pwd_button_css())
        click_continue_button.click()

    def click_continue_login_gm_button(self):
        print("Click continue login button")
        click_continue_login_button = self.driver.find_element_by_xpath(get_continue_login_gmail_button_xpath())
        click_continue_login_button.click()


    def click_logo_facebook(self):
        print("Click logo facebook")
        click_logo_fb = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_logo_facebook_id())))
        click_logo_fb.click()

    def click_icon_home(self):
        print("Click icon home")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
