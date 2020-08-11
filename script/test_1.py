from time import sleep

import allure
import pytest,os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Page.page import Page
from Base import init_driver
from Base.get_data import get_data_2_list
login_list=[("18050388296","5566")]



class Test_Login():

    def setup_class(self):
        self.driver= init_driver.get_driver_by_config("config_1")
        self.login_obj = Page(self.driver).login_obj()

    @allure.feature("首次登录")
    @allure.story("首次登录勾选协议")
    def test_1(self):
        allure.step("点击同意协议按钮")
        self.login_obj.xieyi()
        allure.step("左滑2次")
        sleep(2)
        for i in range(2):
            print("开始滑动")
            self.login_obj.swipe_left()
        #点击立即体验
        allure.step("点击理解体验")
        self.login_obj.tiyan()


        # #输入帐号
        # self.login_obj.input_name(username)
        # #@allure.attach("输入密码",pwd)
        # #输入密码
        # self.login_obj.input_pwd(pwd)
        #勾选协议
        self.login_obj.xieyigouxuan()
        # #点击登录
        # self.login_obj.login_in()
    #@pytest.mark.skipif(2<0)

    #@pytest.mark.skipif(2 < 0)
    @allure.feature("使用错误数据")
    #直接传入一个方法，该方法返回列表类型的字典数据
    @pytest.mark.parametrize("dir",get_data_2_list("data","Login_test1"))
    def test_2(self,dir):
        username=dir["name"]
        pwd=dir["pwd"]
        allure.attach("输入登录帐号", username)
        self.login_obj.input_name(username)

        allure.attach("输入密码", pwd)
        self.login_obj.input_pwd(pwd)
        sleep(1)
        allure.attach("点击登录")
        self.login_obj.login_in()

        allure.attach("判断登录是否成功")
        self.login_obj.assert_login_statu()

    def teardown_class(self):
        self.login_obj.log_out()
        self.driver.quit()
