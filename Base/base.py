from time import sleep
import time,os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.init_driver import get_driver_by_config
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
    def swipe(self, start_x, start_y, end_x, end_y, duration=500):
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
        self.swipe(wight*8/10,height*1/10,wight*1/10,height*1/10)
    # 屏幕右滑
    def swipe_right(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight * 1 / 10, height*1/10, wight * 8 / 10, height*1/10)
    # 屏幕上划
    def swipe_up(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight*1/10 , height* 8 / 10, wight*1/10 , height* 1 / 10)
    # 屏幕下划
    def swipe_down(self):
        wight = self.getSize()[0]
        height = self.getSize()[1]
        self.swipe(wight*1/10 , height* 1 / 10, wight*1/10 , height* 8 / 10)


    # 获取截屏
    def get_screenshot(self, fuc=0, filename="error_shoot",image_name=""):
        if fuc==1:
            filepath= rootpath+os.sep+filename+os.sep+image_name+".png"
        else:
            filepath= rootpath+os.sep+filename+os.sep+time.strftime("%Y-%m-%d-%H：%M：%S")+ ".png"
            print(filepath)
        self.driver.get_screenshot_as_file(filepath)
        return filepath

    def imp_wait(self,mtime=1000):
        self.driver.implicitly_wait(mtime)

    def sleep_time(self,time=2):
        sleep(time)

    def device_time(self):
        return self.driver.device_time

if __name__ == '__main__':
    base = Base(get_driver_by_config("config_2"))
    base.get_screenshot()

