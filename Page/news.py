from selenium.webdriver.common.by import By

from Base.base import Base
#消息 页面类


class News(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_news(self):
        self.find_eles((By.CLASS_NAME,"android.widget.Button"),3).click()