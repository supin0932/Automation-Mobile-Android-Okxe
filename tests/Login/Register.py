from appium import webdriver
import time
import pytest
import unittest
from pages.Get_otp import GetOTP
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import *
from pages.Register_account import *
from appium.webdriver.common.multi_action import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Login_fb import LoginFacebook
from pages.Logout_fb import LogoutFacebook
from pages.Login_gm import LoginGmail
from pages.Logout_gm import LogoutGmail

@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class RegisterAccount(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=get_desired_cap1())
        # self.driver = webdriver.Remote(
        #     command_executor='https://lminhnht_Z0PVgW:YBp4r6LvTMj95us59PuD@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=get_desired_cap())
        self.loginobj = LoginPage1(self.driver)
        self.loginobj1 = LoginPage2(self.driver)
        self.logoutobj = LogoutPage(self.driver)
        self.loginfbobj = LoginFacebook(self.driver)
        self.logoutfbobj = LogoutFacebook(self.driver)
        self.logingmobj = LoginGmail(self.driver)
        self.logoutgmobj = LogoutGmail(self.driver)
        self.registerobj = RegisterAccount(self.driver)
        self.getotp = GetOTP(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_register_with_numberphone(self):
        nb = []
        username = "tester5"
        pwd = "@Aa246357"
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.registerobj.click_button_register()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        self.registerobj.enter_username_register(username=username)
        self.registerobj.enter_pwd_register(pwd=pwd)
        self.registerobj.enter_pwd_confirm_register(pwd=pwd)
        self.registerobj.click_button_enter_register()
        time.sleep(3)
        text = self.getotp.get_otp()
        for i in text[31:37]:
            nb.append(i)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(3)
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.driver.press_keycode(3)
        if text1 == username:
            assert True
        else:
            assert False


    def test_register_with_facebook_unlogin(self):
        nb = []
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
        self.loginfbobj.enter_user_pwd_facebook(username="m.nhutle@okxe.vn", pwd="@Aa246357")
        self.registerobj.click_button_verify_numberphone()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        time.sleep(3)
        text = self.getotp.get_otp()
        for i in text[31:37]:
            nb.append(i)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(3)
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.logoutfbobj.logout_facebook()
        if text1 == "":
            assert True
        else:
            assert False

    def test_register_with_facebook_logined(self):
        nb = []
        self.loginfbobj.login_account_fb(username="m.nhutle@okxe.vn", pwd="@Aa246357")
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
        self.registerobj.click_button_verify_numberphone()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        time.sleep(3)
        text = self.getotp.get_otp()
        for i in text[31:37]:
            nb.append(i)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(3)
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.logoutfbobj.logout_facebook()
        if text1 == "":
            assert True
        else:
            assert False

    def test_register_with_gmail_logined(self):
        nb = []
        self.logingmobj.login_account_gm(username="lenhut20121995@gmail.com", pwd="11762115")
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_gmail()
        self.logingmobj.click_select_account_gmail()
        self.registerobj.click_button_verify_numberphone()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        time.sleep(3)
        text = self.getotp.get_otp()
        for i in text[31:37]:
            nb.append(i)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(3)
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.logoutgmobj.logout_gmail()
        if text1 == "":
            assert True
        else:
            assert False

    def test_register_with_gmail_unlogin(self):
        nb = []
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_gmail()
        self.logingmobj.enter_account_gmail(username="lenhut20121995@gmail.com", pwd="11762115")
        self.registerobj.click_button_verify_numberphone()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        time.sleep(3)
        text = self.getotp.get_otp()
        for i in text[31:37]:
            nb.append(i)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(3)
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.logoutgmobj.logout_gmail()
        if text1 == "":
            assert True
        else:
            assert False

if __name__ == "__main__":
    unittest.main()