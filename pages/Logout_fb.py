from locators.logout import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.multi_action import *
import time
from appium.webdriver.common.touch_action import TouchAction

class LogoutFacebook:
    def __init__(self, driver):
        self.driver = driver

    def logout_facebook(self):
        print("Logout Facebook")
        self.driver.press_keycode(3)
        time.sleep(2)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Facebook"]')))
        CLICK.click()
        # time.sleep(3)

        try:
            CLICK = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.ID, 'com.google.android.gms:id/cancel')))
            CLICK.click()
        except:
            pass
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View[@content-desc="Menu, Tab 6/6"]')))
        CLICK.click()
        action = TouchAction(self.driver)
        time.sleep(2)
        self.driver.swipe(300, 500, 100, 300, 1000)

        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Đăng xuất")))
        CLICK.click()
        time.sleep(5)
        action.tap(x=571, y=279).perform()
        time.sleep(5)
        click_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc='Menu']")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")))
        click_login.click()
        time.sleep(2)
        self.driver.press_keycode(3)
