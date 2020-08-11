from time import sleep
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

    #@pytest.mark.skipif(2<0)
    # @pytest.mark.parametrize("username,pwd",login_list)
    #@allure.feature("首次登录")
    def test_1(self):
        #点击同意协议按钮
        self.login_obj.xieyi()
        #左滑2次
        sleep(1)
        for i in range(2):
            print("开始滑动")
            self.login_obj.swipe_up()
        #点击立即体验
        self.login_obj.tiyan()

        # #@allure.attach("输入登录帐号",username)
        # #输入帐号
        # self.login_obj.input_name(username)
        # #@allure.attach("输入密码",pwd)
        # #输入密码
        # self.login_obj.input_pwd(pwd)
        #勾选协议
        self.login_obj.xieyigouxuan()
        # #点击登录
        # self.login_obj.login_in()

    #@pytest.mark.skipif(2 < 0)
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
        sleep(1)
        # 点击登录
        self.login_obj.login_in()

        # 判断是否登录成功
        self.login_obj.assert_login_statu()

    def teardown_class(self):
        self.login_obj.log_out()
        self.driver.quit()
