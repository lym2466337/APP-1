import Base
from Page.login import Login

class Page():
    def __init__(self,driver):
        self.driver = driver

    def login_obj(self):
        return Login(self.driver)