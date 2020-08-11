from time import sleep
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.init_driver import getDriver
from rootpath import rootpath

class Base():
    # #单例模式
    # def __new__(cls, *args, **kwargs):
    #     cls.instance = None
    #     if not cls.instance:
    #         cls.instances=object.__new__()
    #     return cls.instance

    def __init__(self, driver):
        self.driver = driver

    # 获取单个元素
    def find_ele(self, loc, time=20, fc=0.5):
        print(loc)
        by = loc[0]
        path = loc[1]
        if by == By.XPATH:
            el = WebDriverWait(self.driver, time, fc).until(lambda x: x.find_element_by_xpath(path))
            print("xpath方式定位")
        elif by == "UIcode":
            el = WebDriverWait(self.driver, time, fc).until(lambda x: x.find_element_by_android_uiautomator(path))
            print("uiautomator方式定位")
        else:
            el = WebDriverWait(self.driver, time, fc).until(lambda x: x.find_element(by, path))
            print("其他方式定位")
        print("定位成功")
        return el

    # 获取多个元素
    def find_eles(self, loc, index, time=20, fc=0.5):
        print(loc)
        by = loc[0]
        path = loc[1]
        if by == By.XPATH:
            print(1)
            el = WebDriverWait(self.driver, time, fc).until(lambda x: x.find_elements_by_xpath(path))
        else:
            print(2)
            el = WebDriverWait(self.driver, time, fc).until(lambda x: x.find_elements(by, path))

        print("定位成功")
        return el[index]

    # 输入,fun_index对应多个元素的索引，同时也作为是否获取多个元素的判断
    def input(self, loc, text, fuc_index=10):

        if fuc_index == 10:
            el = self.find_ele(loc)
        else:
            el = self.find_eles(loc, fuc_index)
        el.click()
        el.clear()
        el.send_keys(text)

    # 点击
    def click(self, loc):
        el = self.find_ele(loc)
        el.click()

    # 获取屏幕宽高
    def getSize(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return (width, height)

    # 按坐标滑动
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 按元素滑动到页面结束
    def scroll(self, start_el_loc, end_el_loc, duration=3000):
        self.driver.scroll(start_el_loc, end_el_loc, duration)

    # 按元素滑动到元素位置替换
    def drag_and_drog(self, start_el_loc, end_el_loc):
        self.driver.drag_and_drop(start_el_loc, end_el_loc)

    # 屏幕左滑
    def swipe_left(self):
        wight= self.getSize()[0]
        height= self.getSize()[1]
        self.swipe(wight*4/5,height*1/5,wight*1/5,height*1/5)
    # 屏幕右滑
    def swipe_right(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight * 1 / 5, height*1/5, wight * 4 / 5, height*1/5)
    # 屏幕上划
    def swipe_up(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight*1/5 , height* 4 / 5, wight*1/5 , height* 1 / 5)
    # 屏幕下划
    def swipe_down(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight*1/5 , height* 1 / 5, wight*1/5 , height* 4 / 5)


    # 获取截屏
    def get_screenshot(self, fuc=0, *filename):
        if fuc==1:
            filepath= rootpath+os.sep+"error_shoot"+os.sep+filename+".png"
        else:
            filepath= rootpath+os.sep+"error_shoot"+os.sep+(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))+".png"
        self.driver.get_screenshot_as_file(filepath)

    # 帐号登出
    def log_out(self):
        try:
            # el= self.find_ele(("UIcode",("new UiSelector().text('我的').className('android.widget.TextView')")))
            self.click((By.XPATH, "//android.widget.Button[5]/android.widget.TextView[@text='我的']"))
            sleep(2)

            # w = self.getSize()[0]
            # h = self.getSize()[1]
            # self.swipe(w / 2, h * 4 / 5, w / 2, h * 1 / 5)
            self.swipe_up()
            self.click((By.XPATH, "//*[@text='退出登录']"))

            # self.click(("code", "new UiSelector().resourceId(android:id/button1')"))

            self.click((By.ID, "android:id/button1"))
            assert self.find_ele((By.XPATH, "//*[@text='登 录']"))
            print("登出成功")
            self.get_screenshot()

        except:
            self.get_screenshot()
            print("登出失败")



if __name__ == '__main__':
    base = Base(getDriver())
    base.swipe_up()
