from appium import webdriver
import time
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from pages.Login_fb import LoginFacebook
from pages.Logout_fb import LogoutFacebook
from pages.Login_gm import LoginGmail
from pages.Logout_gm import LogoutGmail



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
        self.loginobj1 = LoginPage2(self.driver)
        self.logoutobj = LogoutPage(self.driver)
        self.loginfbobj = LoginFacebook(self.driver)
        self.logoutfbobj = LogoutFacebook(self.driver)
        self.logingmobj = LoginGmail(self.driver)
        self.logingmobj = LogoutGmail(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_fb_with_account_logined(self):
        """
        Account facebook : True
        Expected : Login successfully
        """
        self.loginfbobj.login_account_fb(username="m.nhutle@okxe.vn", pwd="@Aa246357")
        self.loginobj.click_logo_okxe()
        # try:
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     try:
        #         self.loginobj.click_button_locate_unaccept()
        #     except:
        #         pass
        # except:
        #     pass
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
        time.sleep(10)
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.loginobj1.click_icon_home()
        self.logoutfbobj.logout_facebook()
        if text == "Lê Nhựt":
            assert True
        else:
            assert False


    def test_login_with_fb_with_account_unlogined(self):
        """
        Account facebook : True
        Expected : Login successfully
        """

        self.loginobj.click_logo_okxe()
        # try:
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     try:
        #         self.loginobj.click_button_locate_unaccept()
        #     except:
        #         pass
        # except:
        #     pass
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
        self.loginfbobj.enter_user_pwd_facebook(username="m.nhutle@okxe.vn", pwd="@Aa246357")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.loginobj1.click_icon_home()
        self.logoutfbobj.logout_facebook()
        if text == "Lê Nhựt":
            assert True
        else:
            assert False

    def test_login_with_gmail_with_account_unlogined(self):
        """
        Account gmail : True
        Expected : Login successfully
        """
        self.loginobj.click_logo_okxe()
        # try:
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     try:
        #         self.loginobj.click_button_locate_unaccept()
        #     except:
        #         pass
        # except:
        #     pass
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_gmail()
        self.logingmobj.enter_user_pwd_gmail(username="lenhut20121995@gmail.com", pwd="11762115")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.loginobj1.click_icon_home()
        self.logoutgmobj.logout_gmail()
        if text == "nhựt lê":
            assert True
        else:
            assert False

    def test_login_with_gmail_with_account_logined(self):
        """
        Account facebook : True
        Expected : Login successfully
        """
        self.logingmobj.login_account_gm(username="lenhut20121995@gmail.com", pwd="11762115")
        self.loginobj.click_logo_okxe()
        # try:
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #     try:
        #         self.loginobj.click_button_locate_unaccept()
        #     except:
        #         pass
        # except:
        #     pass
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_gmail()
        self.logingmobj.click_select_account_gmail()
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        self.loginobj1.click_icon_home()
        self.logoutgmobj.logout_gmail()
        if text == "nhựt lê":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
