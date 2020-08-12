from selenium.webdriver.common.by import By
#首页业务元素
element_main_page={
    "deep_button":(By.CLASS_NAME, "android.widget.Button"), #底部所有按钮，0-首页，1-看看，2-购物，3-消息，4-我的
    "change_community_button":(By.XPATH, "//android.view.ViewGroup[2]/android.widget.TextView[3][@text='切换小区']"),
    #切换小区按钮
    "no_change_con":(By.ID, "android:id/button2"),
    #取消切换
    "yes_change_con":(By.ID, "android:id/button1")
    #确认切换
         }

#登录业务元素
element_login={
    "xieyi":(By.XPATH,"//*[@text='同意']"),
    "tiyan":(By.XPATH,"//*[@text='立即体验']"),
    "usr_input":(By.CLASS_NAME,"android.widget.EditText"),  #相同类，0-账号，1-密码
    "pwd_input":(By.CLASS_NAME,"android.widget.EditText"),
    "msg_code":(By.XPATH,"//*[@text='获取手机验证码']"),
    "xieyigouxuan":(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"),
    "login_button":(By.XPATH,"//*[@text='登 录']"),
    "deep_button":(By.CLASS_NAME, "android.widget.Button"), #底部所有按钮，0-首页，1-看看，2-购物，3-消息，4-我的
    "login_out_button":(By.XPATH, "//*[@text='退出登录']"),
    "yes_login_out":(By.ID, "android:id/button1"),
    "succese_login":(By.XPATH, "//*[@text='登录成功']")
}