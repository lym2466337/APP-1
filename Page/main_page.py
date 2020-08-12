from time import sleep

from selenium.webdriver.common.by import By

from Base.base import Base
# 首页类
from Base.init_driver import get_driver_by_config
from Page import element_main_page

class Main_page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击首页
    def click_main(self):
        self.find_ele(element_main_page["deep_button"]).click()

    # 点击看看页面
    def click_look(self):
        self.find_eles(element_main_page["deep_button"], 1).click()

    # 点击购物页面
    def click_shopping(self):
        self.find_eles(element_main_page["deep_button"], 2).click()

    # 点击消息页面
    def click_news(self):
        self.find_eles(element_main_page["deep_button"], 3).click()

    # 点击我的 页面
    def click_my_page(self):
        self.find_eles(element_main_page["deep_button"], 4).click()

    #手动切换小区
    def change_community(self):
        self.click(element_main_page["change_community_button"])

    def look_notice(self):
        pass

    def auto_change_community(self, fuc=0):
        try:
            if fuc == 0:
                self.click(element_main_page["no_change_con"])
                print("拒绝自动切换小区")
            else:
                self.click(element_main_page["yes_change_con"])
                print("自动切换小区")
        except:
            print("未能自动切换小区")


if __name__ == '__main__':
    base = Main_page(get_driver_by_config("config_2"))
    base.click_my_page()
    sleep(2)
    base.click_main()

