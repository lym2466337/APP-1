import os
from appium import webdriver
import yaml
from rootpath import rootpath
def getDriver():
    desired_caps = {
        'platformName': 'Android', # 被测手机是安卓
        'platformVersion': '7.1', # 手机安卓版本
        'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
        'appPackage': 'com.jlbao.app', # 启动APP Package名称
        'appActivity': '.MainActivity', # 启动Activity名称

  # 'appPackage': 'com.android.settings', # 启动APP Package名称
  # 'appActivity': '.Settings',
        'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
        'resetKeyboard': True, # 执行完程序恢复原来输入法
        'noReset': True,       # 不要重置App
        'automationName' : 'UiAutomator2',
        'skipServerInstallation': True
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def get_driver_by_config(config_name):
    filepath = rootpath+os.sep+"Data"+os.sep+"data.yml"
    print(filepath)
    with open(filepath,'r',encoding='utf-8') as f:
        data= yaml.load(f)['DriverConfig']
    data_dir={}
    data_dir=data[config_name]

    desired_caps = {
        'platformName': data_dir['platformName'],
        'platformVersion': data_dir['platformVersion'],
        'deviceName': data_dir['deviceName'],
        'appPackage': data_dir['appPackage'],
        'appActivity': data_dir['appActivity'],
        'unicodeKeyboard': data_dir['unicodeKeyboard'],
        'resetKeyboard': data_dir['resetKeyboard'],
        'noReset': data_dir['noReset'],
        'automationName': data_dir['automationName'],
        'skipServerInstallation': data_dir['skipServerInstallation']
    }
    print(desired_caps)
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

if __name__ == '__main__':
    get_driver_by_config("config_1")

