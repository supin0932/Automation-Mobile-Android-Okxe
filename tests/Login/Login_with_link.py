from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import *
from appium.webdriver.extensions.applications import Applications
from appium.options.android import UiAutomator2Options
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
        self.driver.close_app()

    # def test_login_with_fb_with_account_logined(self):
    #     """
    #     Username : True
    #     Password : True
    #     Expected : Login successfully
    #     """
    #
    #     '''Đăng nhập facebook'''
    #     self.loginobj1.click_icon_facebook()
    #     time.sleep(10)
    #     self.driver.find_element(MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']").send_keys(
    #         "m.nhut@okxe.vn")
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Password").send_keys("@Aa246357")
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In").click()
    #     self.driver.press_keycode(3)
    #
    #     '''Đăng nhập okxe'''
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         try:
    #             self.loginobj.click_button_locate_unaccept()
    #         except:
    #             pass
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #     self.loginobj1.click_icon_facebook()
    #     time.sleep(10)
    #     self.loginobj.click_logo_account()
    #     text = self.loginobj.get_text_username_account()
    #     self.driver.press_keycode(3)
    #
    #     '''Logout facebook'''
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Facebook").click()
    #     time.sleep(3)
    #     self.driver.find_element(MobileBy.XPATH, "//android.view.View[@content-desc='Menu, tab 6 of 6']").click()
    #     action = TouchAction(self.driver)
    #     time.sleep(1)
    #     action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
    #     for i in range(1):
    #         action = TouchAction(self.driver)
    #         action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
    #         time.sleep(1)
    #
    #     self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Log out']").click()
    #     time.sleep(5)
    #     action.tap(x=571, y=279).perform()
    #     time.sleep(2)
    #     click_login = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc='Menu']")))
    #     click_login.click()
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]").click()
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]").click()
    #     time.sleep(2)
    #     self.driver.press_keycode(3)
    #     if text == "Xuân Ánh":
    #             assert True
    #     else:
    #         assert False

    def test_login_with_fb_with_account_unlogined(self):

        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Gmail").click()
        time.sleep(2)
        self.driver.find_element(MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd").click()
        time.sleep(2)
        self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        time.sleep(2)
        self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        time.sleep(5)
        action = TouchAction(self.driver)
        action.tap(x=125, y=777).perform()
        time.sleep(3)
        self.driver.find_element(MobileBy.ID, "00000000-0000-0462-0000-010500000107").send_keys("luv201295@gmail.com")

        # self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView").click()
        # time.sleep(3)
        # self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]").click()
        # time.sleep(3)
        # self.driver.find_element(MobileBy.ID, "com.android.settings:id/button").click()
        # time.sleep(3)
        # self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        # time.sleep(3)
        # self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        # self.driver.press_keycode(3)
    # def test_login_with_fb_with_account_unlogined(self):
    #     """
    #     Username : True
    #     Password : True
    #     Expected : Login successfully
    #     """
    #     '''Đăng nhập okxe'''
    #     self.loginobj.click_logo_okxe()
    #     try:
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_next_banner()
    #         self.loginobj.click_button_complete_banner()
    #         try:
    #             self.loginobj.click_button_locate_unaccept()
    #         except:
    #             pass
    #     except:
    #         pass
    #     self.loginobj.click_button_login()
    #
    #     '''Đăng nhập facebook'''
    #     self.loginobj1.click_icon_facebook()
    #     time.sleep(10)
    #     self.driver.find_element(MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']").send_keys("m.nhut@okxe.vn")
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Password").send_keys("@Aa246357")
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In").click()
    #     time.sleep(10)
    #
    #     self.loginobj.click_logo_account()
    #     text = self.loginobj.get_text_username_account()
    #     self.driver.press_keycode(3)
    #
    #     '''Logout facebook'''
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Facebook").click()
    #     time.sleep(3)
    #     self.driver.find_element(MobileBy.XPATH, "//android.view.View[@content-desc='Menu, tab 6 of 6']").click()
    #     action = TouchAction(self.driver)
    #     time.sleep(1)
    #     action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
    #     for i in range(1):
    #         action = TouchAction(self.driver)
    #         action.press(x=537, y=1964).move_to(x=592, y=347).release().perform()
    #         time.sleep(1)
    #
    #     self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Log out']").click()
    #     time.sleep(5)
    #     action.tap(x=571, y=279).perform()
    #     time.sleep(2)
    #     click_login = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc='Menu']")))
    #     click_login.click()
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]").click()
    #     time.sleep(2)
    #     self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]").click()
    #     time.sleep(2)
    #     self.driver.press_keycode(3)
    #     if text == "Xuân Ánh":
    #             assert True
    #     else:
    #         assert False




if __name__ == "__main__":
    unittest.main()
