import unittest
import pytest
from appium import webdriver
from pages.Login_with_link import LoginPage2
from pages.Login_with_username_pwd import *
from pages.Logout import *
from utils.driversManages import *
from appium.webdriver.common.mobileby import MobileBy
import time


@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest1(unittest.TestCase):

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

    def tearDown(self):
        self.driver.quit()

    def test_login_with_usr_is_true_pw_is_true(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get username
        Step 4 : Logout account
        Step 5 : Compare with expected result
        *************************
        Data : + Username : True
               + Password : True
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="0932949905")
        self.loginobj.enter_button_pwd(pwd="@Aa246357")
        self.loginobj.click_button_enter_login()
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.driver.terminate_app('com.okxe.app')
        if text == "Lê Minh Nhựt":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pw_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : Fasle
               + Password : Fasle
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="09322415744")
        self.loginobj.enter_button_pwd(pwd="@Aa24635777")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Tên đăng nhập không tồn tại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_true_pw_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : True
               + Password : False
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="0932241574")
        self.loginobj.enter_button_pwd(pwd="@Aa2463577")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pw_is_true(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : False
               + Password : True
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="09322415744")
        self.loginobj.enter_button_pwd(pwd="@Aa246357")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Tên đăng nhập không tồn tại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_empty_pw_is_empty(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : Empty
               + Password : Empty
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="")
        self.loginobj.enter_button_pwd(pwd="")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_empty_pwd_is_true(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : Empty
               + Password : True
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="")
        self.loginobj.enter_button_pwd(pwd="@Aa246357")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False


    def test_login_with_usr_is_true_pwd_is_empty(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : True
               + Password : Empty
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="0932241574")
        self.loginobj.enter_button_pwd(pwd="")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pwd_is_empty(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : False
               + Password : Empty
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="@0932241574")
        self.loginobj.enter_button_pwd(pwd="")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_empty_pwd_is_false(self):
        """
        Step 1 : Open website OKXE
        Step 2 : Login account
        Step 3 : Get text warning
        Step 4 : Compare with expected result
        *************************
        Data : + Username : Empty
               + Password : False
        Expected Result : Login unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        try:
            wait = WebDriverWait(self.driver, 10)
            click_login = wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/imageButton_noticeDialog_close")))
            click_login.click()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     self.loginobj.click_button_locate_unaccept()
        #
        except:
            pass
        time.sleep(5)
        self.loginobj.click_button_login()
        self.loginobj.enter_button_usr(usr="")
        self.loginobj.enter_button_pwd(pwd="12345678")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
