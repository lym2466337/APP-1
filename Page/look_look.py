from Base.base import Base
from Page import element_main_page
#我的 页面类


class Look_look(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_look(self):
        self.find_eles(element_main_page["deep_button"], 1).click()
