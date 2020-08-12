from Page import element_main_page
from Base.base import Base
#我的 页面类


class Shopping(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_shopping(self):
        self.find_eles(element_main_page["deep_button"],2).click()