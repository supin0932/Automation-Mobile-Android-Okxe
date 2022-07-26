from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Logout import *
from pages.Logout import *


@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest2(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=get_desired_cap1())
        # self.driver = webdriver.Remote(
        #     command_executor='https://lminhnht_Z0PVgW:YBp4r6LvTMj95us59PuD@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=get_desired_cap())
        self.loginobj = LoginPage1(self.driver)
        self.logoutobj = LogoutPage(self.driver)
        self.logoutobj = LogoutPage(self.driver)

    def tearDown(self):
        self.driver.close_app()

    def test_login_with_usr_pw_is_true(self):
        """
        Username : True
        Password : True
        Expected : Login successfully
        """
        self.loginobj.click_logo_okxe()
        try :
            self.loginobj.click_button_next_banner()
            self.loginobj.click_button_next_banner()
            self.loginobj.click_button_complete_banner()
            self.loginobj.click_button_locate_unaccept()

        except :
            pass
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="0932241574")
        self.loginobj.enter_button_pwd(pwd="@Aa246357")
        self.loginobj.click_button_enter_login()
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        if text == "nhut le":
            assert True
        else:
            assert False

    # def test_login_with_usr_is_true_pw_is_false(self):
    #     """
    #     Username : True
    #     Password : False
    #     Expected : Login unsuccessfully
    #     """
    #     # self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         self.loginobj.click_button_locate_unaccept()
    #
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj.enter_button_usr(usr="0932241574")
    #     self.loginobj.enter_button_pwd(pwd="@Aa2463577")
    #     self.loginobj.click_button_enter_login()
    #     text = self.loginobj.get_text_warning()
    #     if text == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
    #         assert True
    #     else:
    #         assert False

    # def test_login_with_usr_is_false_pw_is_true(self):
    #     """
    #     Username : False
    #     Password : True
    #     Expected : Login unsuccessfully
    #     """
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         self.loginobj.click_button_locate_unaccept()
    #
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj.enter_button_usr(usr="09322415744")
    #     self.loginobj.enter_button_pwd(pwd="@Aa246357")
    #     self.loginobj.click_button_enter_login()
    #     text = self.loginobj.get_text_warning()
    #     if text == "Tên đăng nhập không tồn tại.":
    #         assert True
    #     else:
    #         assert False
    #
    # def test_login_with_usr_pw_is_empty(self):
    #     """
    #     Username : Empty
    #     Password : Empty
    #     Expected : Login unsuccessfully
    #     """
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         self.loginobj.click_button_locate_unaccept()
    #
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj.enter_button_usr(usr="")
    #     self.loginobj.enter_button_pwd(pwd="")
    #     self.loginobj.click_button_enter_login()
    #     text = self.loginobj.get_text_warning()
    #     print(text)
    #     if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
    #         assert True
    #     else:
    #         assert False
    #
    # def test_login_with_usr_is_empty(self):
    #     """
    #     Username : Empty
    #     Password : True
    #     Expected : Login unsuccessfully
    #     """
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         self.loginobj.click_button_locate_unaccept()
    #
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj.enter_button_usr(usr="")
    #     self.loginobj.enter_button_pwd(pwd="@Aa246357")
    #     self.loginobj.click_button_enter_login()
    #     text = self.loginobj.get_text_warning()
    #     print(text)
    #     self.driver.close_app()
    #     if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
    #         assert True
    #     else:
    #         assert False
    #
    #
    # def test_login_with_pwd_is_empty(self):
    #     """
    #     Username : True
    #     Password : Empty
    #     Expected : Login unsuccessfully
    #     """
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         self.loginobj.click_button_locate_unaccept()
    #
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj.enter_button_usr(usr="0932241574")
    #     self.loginobj.enter_button_pwd(pwd="")
    #     self.loginobj.click_button_enter_login()
    #     text = self.loginobj.get_text_warning()
    #     print(text)
    #     if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
    #         assert True
    #     else:
    #         assert False
    #

if __name__ == "__main__":
    unittest.main()
