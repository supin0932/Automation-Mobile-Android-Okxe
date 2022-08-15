from appium import webdriver
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
        self.logoutgmobj = LogoutGmail(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_fb_with_account_logined(self):
        """
        Step 1 : Open app Facebook
        Step 2 : Login account facebook
        Step 3 : Open app OKXE
        Step 4 : Click button login
        Step 5 : Click button link with facebook
        Step 6 : Select account facebook
        Step 7 : Get info account
        Step 8 : Logout account okxe
        Step 9 : Logout account facebook
        Step 10 : Verify info account
        *************************
        Data : + Account facebook : Correct
        Expected Result : Login successfull
        """
        self.loginfbobj.login_account_fb(username="m.nhutle@okxe.vn", pwd="@Aa246357")
        self.loginobj.click_logo_okxe()
        try:
            self.loginobj.click_button_next_banner()
            self.loginobj.click_button_next_banner()
            self.loginobj.click_button_complete_banner()
            try:
                self.loginobj.click_button_locate_unaccept()
            except:
                pass
        except:
            pass
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
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


    def   test_login_with_fb_with_account_unlogined(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button link with facebook
        Step 4 : Login account facebook
        Step 5 : Get info account
        Step 7 : Logout account okxe
        Step 8 : Open app Facebook
        Step 9 : Logout account facebook
        Step 10 : Verify info account
        *************************
        Data : + Account facebook : Correct
        Expected Result : Login successfull
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
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button link with gmail
        Step 4 : Login account gmail
        Step 5 : Get info account
        Step 7 : Logout account okxe
        Step 8 : Open app Gmail
        Step 9 : Logout account gmail
        Step 10 : Verify info account
        *************************
        Data : + Account gmail : Correct
        Expected Result : Login successfull
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
        self.logingmobj.enter_account_gmail(username="lenhut20121995@gmail.com", pwd="11762115")
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
        Step 1 : Open app Gmail
        Step 2 : Login account gmail
        Step 3 : Open app OKXE
        Step 4 : Click button login
        Step 5 : Click button link with gmail
        Step 6 : Select account gmail
        Step 7 : Get info account
        Step 8 : Logout account okxe
        Step 9 : Logout account gmail
        Step 10 : Verify info account
        *************************
        Data : + Account gmail : Correct
        Expected Result : Login successfull
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
