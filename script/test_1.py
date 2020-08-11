from time import sleep
import pytest,os,sys
from Tools.scripts.var_access_benchmark import B
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Page.page import Page
from Base.init_driver import getDriver
from Base.get_data import get_data_2_list
login_list=[("18050388296","5566")]


class Test:

    def setup_class(self):
        self.driver= getDriver()
        self.login_obj = Page(self.driver).login_obj()


    #@pytest.mark.skipif(1<0)
    @pytest.mark.parametrize("username,pwd",login_list)
    #@allure.feature("首次登录")
    def test_1(self,username,pwd):
        #点击同意协议按钮
        self.login_obj.xieyi()
        #左滑2次
        sleep(1)
        for i in range(0,2):
            self.login_obj.swipe((500,200,50,200,600))
        #点击立即体验
        self.login_obj.tiyan()

        #@allure.attach("输入登录帐号",username)
        #输入帐号
        self.login_obj.input_name(username)
        #@allure.attach("输入密码",pwd)
        #输入密码
        self.login_obj.input_pwd(pwd)
        #勾选协议
        self.login_obj.xieyigouxuan()
        #点击登录
        self.login_obj.login_in()

    #使用错误数据登录失败
    #直接传入一个方法，该方法返回列表类型的字典数据
    @pytest.mark.parametrize("dir",get_data_2_list("data","Login_test1"))
    def test_2(self,dir):
        # @allure.attach("输入登录帐号",username)
        # 输入帐号
        self.login_obj.input_name(dir["name"])
        # @allure.attach("输入密码",pwd)
        # 输入密码
        self.login_obj.input_pwd(dir["pwd"])
        sleep(2)
        # 点击登录
        self.login_obj.login_in()

        # 判断是否登录成功
        self.login_obj.assert_login_statu()

    def teardown_class(self):
        self.login_obj.log_out()
        self.driver.quit()
