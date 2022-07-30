from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.multi_action import *
import time
from appium.webdriver.common.touch_action import TouchAction

class LogoutGmail:
    def __init__(self, driver):
        self.driver = driver

    def logout_gmail(self):
        self.driver.press_keycode(3)
        print("Logout Gmail")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_apd_ring_view")))
        CLICK.click()
        time.sleep(3)
        TouchAction(self.driver).tap(x=518, y=1203).perform()
        time.sleep(3)
        TouchAction(self.driver).tap(x=488, y=357).perform()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.android.settings:id/button")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        CLICK.click()
        self.driver.press_keycode(3)