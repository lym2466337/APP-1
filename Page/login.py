from time import sleep
from Page import element_login
from Base.base import Base
from Base.init_driver import getDriver

"""
    登录功能页面
"""


class Login(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def xieyi(self):
        self.click(element_login["xieyi"])
        print("同意协议")

    def tiyan(self):
        self.click(element_login["tiyan"])
        print("点击立即体验")

    def input_name(self, username):
        # 输入帐号
        self.input(element_login["usr_input"], username, 0)
        print("输入帐号")

    def input_pwd(self, pwd):
        # 输入密码
        self.input(element_login["pwd_input"], pwd, 1)
        print("输入密码")

    def xieyigouxuan(self):
        self.click(element_login["xieyigouxuan"])
        print("勾选协议")

    def login_in(self):
        self.click(element_login["login_button"])

    def log_out(self):
        try:
            # el= self.find_ele(("UIcode",("new UiSelector().text('我的').className('android.widget.TextView')")))
            self.find_eles(element_login["deep_button"],4).click()
            sleep(2)

            # w = self.getSize()[0]
            # h = self.getSize()[1]
            # self.swipe(w / 2, h * 4 / 5, w / 2, h * 1 / 5)
            self.swipe_up()
            self.click(element_login["login_out_button"])

            # self.click(("code", "new UiSelector().resourceId(android:id/button1')"))

            self.click(element_login["yes_login_out"])
            assert self.find_ele(element_login["login_button"])
            print("登出成功")

        except:
            self.get_screenshot()
            print("登出失败")

    def assert_login_statu(self):
        try:
            assert self.find_ele(element_login["succese_login"], 5)
            print("登录成功")
        except:
            print("登录失败")


if __name__ == '__main__':
    login = Login(getDriver())
    login.tiyan()
