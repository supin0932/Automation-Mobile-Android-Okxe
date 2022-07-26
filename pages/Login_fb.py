from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction

class LoginFacebook:
    def __init__(self, driver):
        self.driver = driver


    def login_account_fb(self, username, pwd):
        print("Login account facebook")
        self.driver.press_keycode(3)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@content-desc="Facebook"]')))
        CLICK.click()
        time.sleep(5)
        action = TouchAction(self.driver)
        action.tap(x=330, y=861).perform()
        time.sleep(2)
        action.tap(x=330, y=861).perform()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']")))
        CLICK.send_keys(username)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Password")))
        CLICK.send_keys(pwd)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Log In")))
        CLICK.click()
        time.sleep(5)
        self.driver.press_keycode(3)

    def enter_user_pwd_facebook(self, username, pwd):
        print("Enter account facebook")
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.EditText[@content-desc='Username']")))
        CLICK.send_keys(username)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Password")))
        CLICK.send_keys(pwd)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Log In")))
        CLICK.click()