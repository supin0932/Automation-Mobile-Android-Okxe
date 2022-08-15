

def get_desired_cap1():
    desired_cap = {
      "platformName": "Android",
      "appium:platformVersion": "10.0",
      "appium:deviceName": "Galaxy Note2Note0 Ultra Ultra 5G",
      "appium:automationName": "UiAutomator2",
      "appium:udid": "192.168.0.26:5555"
    }
    return desired_cap


def get_desired_cap():
    desired_cap = {
        # Set your access credentials
        "browserstack.user": "lminhnht_Z0PVgW",
        "browserstack.key": "YBp4r6LvTMj95us59PuD",

        # Set URL of the application under test
        "app": "bs://c817d1d902b0d5e39b26b2dadc962dbc7d3d5018",

        # Specify device and os_version for testing
        "platformName": "android",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",

        # Set other BrowserStack capabilities
        "project": "First Python project",
        "build": "browserstack-build-1",
        "name": "first_test"
    }
    return desired_cap
