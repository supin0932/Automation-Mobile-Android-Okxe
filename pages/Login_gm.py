from locators.logout import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction

class LoginGmail:
    def __init__(self, driver):
        self.driver = driver


    def login_account_gm(self, username, pwd):
        print("Login account gmail.com")
        self.driver.press_keycode(3)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd")))
        CLICK.click()
        time.sleep(3)
        TouchAction(self.driver).tap(x=460, y=913).perform()
        time.sleep(3)
        TouchAction(self.driver).tap(x=257, y=594).perform()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys(username)
        time.sleep(1)
        TouchAction(self.driver).tap(x=896, y=2082).perform()
        time.sleep(2)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys(pwd)
        time.sleep(2)
        TouchAction(self.driver).tap(x=899, y=1233).perform()
        time.sleep(5)
        TouchAction(self.driver).tap(x=884, y=1524).perform()
        time.sleep(10)
        self.driver.press_keycode(3)

    def enter_account_gmail(self, username, pwd):
        print("Enter account gmail")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()
        time.sleep(10)
        action = TouchAction(self.driver)
        action.tap(x=149, y=682).perform()
        time.sleep(1)
        action.tap(x=149, y=682).perform()
        time.sleep(1)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys(username)
        time.sleep(1)
        action.tap(x=572, y=647).perform()
        time.sleep(1)
        action.tap(x=572, y=647).perform()
        time.sleep(2)
        self.driver.press_keycode(66)
        time.sleep(5)
        action.tap(x=572, y=647).perform()
        time.sleep(1)
        action.tap(x=572, y=647).perform()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.EditText")))
        CLICK.send_keys(pwd)
        time.sleep(2)
        self.driver.press_keycode(66)
        time.sleep(3)
        action.tap(x=859, y=1571).perform()
        time.sleep(1)
        action.tap(x=859, y=1571).perform()
        time.sleep(2)

    def click_select_account_gmail(self):
        print("Select account")
        time.sleep(5)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()
