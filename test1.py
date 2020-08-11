from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.base import Base
from uiautomator import device as d


# desired_caps = {
#   'platformName': 'Android', # 被测手机是安卓
#   'platformVersion': '7.1', # 手机安卓版本
#   'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
#   'appPackage': 'com.jlbao.app', # 启动APP Package名称
#   'appActivity': '.MainActivity', # 启动Activity名称
#
#   # 'appPackage': 'com.android.settings', # 启动APP Package名称
#   # 'appActivity': '.Settings',
#   'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
#   'resetKeyboard': True, # 执行完程序恢复原来输入法
#   'noReset': True,       # 不要重置App
#   'automationName' : 'UiAutomator2'
# }
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

d(text="登录",className="android.view.ViewGroup").click()







