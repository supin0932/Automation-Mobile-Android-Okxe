import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from pages.Forget_id_and_pwd import *
from pages.Get_otp import *
from appium.webdriver.common.mobileby import MobileBy


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
        self.forgetpwdobj = ForgetPassword(self.driver)
        self.getotp = GetOTP(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_forget_pwd_id_with_numberphone_registed_OTPcorrect(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Enter opt to sms
        Step 6 : Get username
        Step 7 : Get password
        Step 8 : Enter username and password at login
        Step 9 : Verify account
        *************************
        Data : + Numberphone : Correct
               + OTP : Correct
        Expected Result : Regiter successfull
        """
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone="0932241574")
        self.forgetpwdobj.click_button_continue()
        time.sleep(10)
        text = self.getotp.get_otp()
        nb = []
        print(text)
        for i in text[31:37]:
            nb.append(i)
        print(nb)
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.forgetpwdobj.enter_otp(n1=nb[0], n2=nb[1], n3=nb[2], n4=nb[3], n5=nb[4], n6=nb[5])
        time.sleep(4)
        self.forgetpwdobj.click_tab_username()
        pwdnew = "@Aa246357"
        username = self.forgetpwdobj.get_username()
        self.forgetpwdobj.click_tab_pwd()
        self.forgetpwdobj.enter_pwd(pwd=pwdnew)
        self.forgetpwdobj.enter_pwd_confirm(pwdcf=pwdnew)
        self.forgetpwdobj.click_button_update_pwd()
        self.forgetpwdobj.click_button_comback_login()
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
        if text1 == "nhut le":
            assert True
        else:
            assert False

    def test_forget_pwd_id_with_numberphone_registed_OTPuncorrect(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Enter opt any
        Step 6 : Verify page
        *************************
        Data : + Numberphone : Correct
               + OTP : UnCorrect
        Expected Result : Regiter unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone="0932241574")
        self.forgetpwdobj.click_button_continue()
        self.forgetpwdobj.enter_otp(n1=1, n2=2, n3=3, n4=4, n5=5, n6=6)
        text = self.forgetpwdobj.get_text_warning()
        self.forgetpwdobj.click_button_back()
        self.forgetpwdobj.click_button_back()
        self.forgetpwdobj.click_button_close()
        self.driver.press_keycode(3)
        if text == "Mã xác thực OTP":
            assert True
        else:
            assert False

    def test_forget_pwd_id_with_numberphone_not_registed(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Verify page
        *************************
        Data : + Numberphone : Not registed
        Expected Result : Regiter unsuccessfull
        """
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone="0932949405")
        self.forgetpwdobj.click_button_continue()
        time.sleep(5)
        text = self.forgetpwdobj.get_text_warning()
        self.forgetpwdobj.click_button_back()
        self.forgetpwdobj.click_button_close()
        self.driver.press_keycode(3)
        if text == "Quên ID/Mật khẩu":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
