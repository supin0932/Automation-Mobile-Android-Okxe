from locators.logout import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

class GetOTP:
    def __init__(self, driver):
        self.driver = driver


    def get_otp(self):
        print("Get OTP")
        self.driver.press_keycode(3)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Nhắn tin")))
        CLICK.click()
        time.sleep(3)
        Get_otp = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[5]"))).text

        click_mess = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[5]")))
        click_mess.click()

        time.sleep(2)
        TouchAction(self.driver).tap(x=1022, y=150).perform()

        click_delete_mess = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")))
        click_delete_mess.click()

        time.sleep(2)
        TouchAction(self.driver).tap(x=892, y=1261).perform()
        self.driver.press_keycode(3)
        return Get_otp


