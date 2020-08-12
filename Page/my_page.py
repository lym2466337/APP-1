from Page import element_main_page
from Base.base import Base
#我的 页面类


class My_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_my_page(self):
        self.find_eles(element_main_page["deep_button"],4).click()

