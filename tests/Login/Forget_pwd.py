from appium import webdriver
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from pages.Forget_id_and_pwd import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction
from pages.Get_otp import *

@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class ForgetPWD(unittest.TestCase):

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
        self.forgetobj = ForgetPassword(self.driver)
        self.getotp = GetOTP(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_forget_pwd(self):
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetobj.click_button_forget_pwd()
        self.forgetobj.enter_numberphone(numberphone="0772641940")
        self.forgetobj.click_button_continue()
        time.sleep(3)
        text = self.getotp.get_otp()
        nb = []
        print(text)
        for i in text[31:37]:
            nb.append(i)
        print(nb)
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.forgetobj.enter_otp(n1=nb[0],n2=nb[1],n3=nb[2],n4=nb[3],n5=nb[4],n6=nb[5])
        time.sleep(3)
        self.forgetobj.click_tab_username()
        pwdnew = "@Aa246357"
        username = self.forgetobj.get_username()
        self.forgetobj.click_tab_pwd()
        self.forgetobj.enter_pwd(pwd=pwdnew)
        self.forgetobj.enter_pwd_confirm(pwdcf=pwdnew)
        self.forgetobj.click_button_continue()
        self.forgetobj.click_button_update_pwd()
        self.forgetobj.click_button_comback_login()
        self.loginobj.enter_button_usr(usr=username)
        self.loginobj.enter_button_pwd(pwd=pwdnew)
        self.loginobj.click_button_enter_login()
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        time.sleep(2)
        self.driver.press_keycode(3)
        if text1 == "tester2":
            assert True
        else:
            assert False

if __name__ == "__main__":
    unittest.main()