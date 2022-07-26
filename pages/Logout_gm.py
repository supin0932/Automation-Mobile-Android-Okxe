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
        """Đăng xuất gmail"""
        print("Logout Gmail")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Gmail")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gm:id/og_selected_account_disc_apd")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.android.settings:id/button")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        CLICK.click()
        self.driver.press_keycode(3)