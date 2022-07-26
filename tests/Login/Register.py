from appium import webdriver
import time
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from appium.webdriver.common.multi_action import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def tearDown(self):
        self.driver.quit()

    def test_register_with_numberphone(self):
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/tv_register')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/edt_phone_number')))
        CLICK.send_keys("enter numberphone")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_continue')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText')))
        CLICK.send_keys("enter username")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText')))
        CLICK.send_keys("enter pwd")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText')))
        CLICK.send_keys("enter pwd again")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_register')))
        CLICK.send_keys("cick register")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]')))
        CLICK.send_keys("")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
        self.driver.press_keycode(3)
        if text == "nhut le":
            assert True
        else:
            assert False


    def test_register_with_facebook_unlogin(self):
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_facebook()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']")))
        CLICK.send_keys("m.nhutle@okxe.vn")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Password")))
        CLICK.send_keys("@Aa246357")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Log In")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/btn_confirm_base")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/edt_phone_number')))
        CLICK.send_keys("enter numberphone")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_continue')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]')))
        CLICK.send_keys("")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
        self.driver.press_keycode(3)
        time.sleep(5)

        '''Logout facebook'''
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Facebook"]')))
        CLICK.click()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View[@content-desc="Menu, tab 5 of 5"]')))
        CLICK.click()
        action = TouchAction(self.driver)
        time.sleep(1)
        action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
        for i in range(1):
            action = TouchAction(self.driver)
            action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
            time.sleep(1)

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Log out']")))
        CLICK.click()
        time.sleep(5)
        action.tap(x=571, y=279).perform()
        time.sleep(2)
        click_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc='Menu']")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")))
        click_login.click()
        time.sleep(2)
        self.driver.press_keycode(3)
        if text == "nhut le":
            assert True
        else:
            assert False
    def test_register_with_facebook_logined(self):
        '''Đăng nhập facebook'''
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Facebook"]')))
        CLICK.click()
        time.sleep(5)
        action = TouchAction(self.driver)
        action.tap(x=330, y=861).perform()
        time.sleep(2)
        action.tap(x=330, y=861).perform()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']")))
        CLICK.send_keys("m.nhutle@okxe.vn")
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Password")))
        CLICK.send_keys("@Aa246357")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Log In")))
        CLICK.click()
        time.sleep(5)
        self.driver.press_keycode(3)

        '''Đăng nhập okxe'''
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
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/btn_confirm_base")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/edt_phone_number')))
        CLICK.send_keys("enter numberphone")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_continue')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]')))
        CLICK.send_keys("")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
        self.driver.press_keycode(3)
        time.sleep(5)

        '''Logout facebook'''
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Facebook"]')))
        CLICK.click()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View[@content-desc="Menu, tab 5 of 5"]')))
        CLICK.click()
        action = TouchAction(self.driver)
        time.sleep(1)
        action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
        for i in range(1):
            action = TouchAction(self.driver)
            action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
            time.sleep(1)

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Log out']")))
        CLICK.click()
        time.sleep(5)
        action.tap(x=571, y=279).perform()
        time.sleep(2)
        click_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc='Menu']")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")))
        click_login.click()
        time.sleep(2)
        self.driver.press_keycode(3)
        if text == "nhut le":
            assert True
        else:
            assert False

    def test_register_with_gmail_logined(self):
        """ Đăng nhập gmail """
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd")))
        CLICK.click()
        time.sleep(5)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout")))
        CLICK.click()
        action = TouchAction(self.driver)
        action.tap(x=125, y=777).perform()
        time.sleep(2)
        action.tap(x=125, y=777).perform()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys("lenhut20121995@gmail.com")
        time.sleep(2)
        action.tap(x=125, y=777).perform()
        time.sleep(1)
        action.tap(x=125, y=777).perform()
        time.sleep(1)
        self.driver.press_keycode(66)
        time.sleep(2)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys("11762115")
        time.sleep(5)
        self.driver.press_keycode(66)
        time.sleep(3)
        action.tap(x=884, y=1524).perform()
        time.sleep(10)
        self.driver.press_keycode(3)

        '''Đăng nhập okxe'''
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
        time.sleep(20)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/btn_confirm_base")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/edt_phone_number')))
        CLICK.send_keys("enter numberphone")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_continue')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]')))
        CLICK.send_keys("")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
        self.driver.press_keycode(3)
        time.sleep(5)

        '''Logout facebook'''
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.android.settings:id/button")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        CLICK.click()

        self.driver.press_keycode(3)
        if text == "nhut le":
            assert True
        else:
            assert False

    def test_register_with_gmail_unlogin(self):
        self.driver.press_keycode(3)
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.loginobj1.click_icon_gmail()
        """Đăng nhập gmail"""
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()
        action = TouchAction(self.driver)
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys("lenhut20121995@gmail.com")
        time.sleep(1)
        action.tap(x=125, y=777).perform()
        time.sleep(1)
        action.tap(x=125, y=777).perform()
        time.sleep(2)
        time.sleep(2)
        self.driver.press_keycode(66)
        time.sleep(5)
        action.tap(x=125, y=777).perform()
        time.sleep(1)
        action.tap(x=125, y=777).perform()
        CLICK = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys("11762115")
        time.sleep(2)
        self.driver.press_keycode(66)
        time.sleep(3)
        action.tap(x=879, y=1533).perform()
        time.sleep(1)
        action.tap(x=879, y=1533).perform()
        time.sleep(5)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.okxe.app:id/btn_confirm_base")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/edt_phone_number')))
        CLICK.send_keys("enter numberphone")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, 'com.okxe.app:id/btn_continue')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]')))
        CLICK.send_keys("")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]')))
        CLICK.send_keys("")
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Trang chủ")))
        CLICK.click()
        self.driver.press_keycode(3)
        time.sleep(5)

        '''Logout facebook'''
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.android.settings:id/button")))
        CLICK.click()

        CLICK = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        CLICK.click()
        self.driver.press_keycode(3)
        if text == "nhut le":
            assert True
        else:
            assert False