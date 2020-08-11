from selenium.webdriver.common.by import By
from Base.base import Base
from Base.init_driver import getDriver
"""
    登录
    协议同意按钮：By.XPATH,"//*[@text='同意']"
    帐号栏位：By.CLASS_NAME,"android.widget.EditText"
    密码栏位：By.CLASS_NAME,"android.widget.EditText"
    #会同时查出2个元素后，按索引获取指定元素
    短信验证码按钮：By.XPATH,"//*[@text='获取手机验证码']"
    协议勾选按钮：By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView
"
    登录按钮：By.XPATH,"//*[@text='登 录']"
"""
class Login(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def xieyi(self):
        self.click((By.XPATH,"//*[@text='同意']"))
        print("同意协议")
    def tiyan(self):
        self.click((By.XPATH,"//*[@text='立即体验']"))
        print("点击立即体验")
    def input_name(self,username):
        #输入帐号
        self.input((By.CLASS_NAME,"android.widget.EditText"),username,0)
        print("输入帐号")
    def input_pwd(self,pwd):
        #输入密码
        self.input((By.CLASS_NAME,"android.widget.EditText"),pwd,1)
        print("输入密码")
    def xieyigouxuan(self):
        self.click((By.XPATH,"/hierarchy/android.widget.FrameLayout/"
                             "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/"
                             "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                             "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                             "android.view.ViewGroup[2]/android.widget.ImageView"))
        print("勾选协议")
    def login_in(self):
        self.click((By.XPATH,"//*[@text='登 录']"))


    def assert_login_statu(self):
        try:
            assert self.find_ele((By.XPATH,"//*[@text='登录成功']"),5)
            print("登录成功")
        except:
            print("登录失败")


if __name__ == '__main__':
    login = Login(getDriver())
    login.tiyan()