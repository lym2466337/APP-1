from Page import login,look_look,main_page,news,shopping,my_page

class Page():
    def __init__(self,driver):
        self.driver = driver

    def login_obj(self):
        return login.Login(self.driver)

    def look_look_obj(self):
        return look_look.Look_look(self.driver)

    def main_page_obj(self):
        return main_page.Main_page(self.driver)

    def news_obj(self):
        return news.News(self.driver)

    def shopping_obj(self):
        return shopping.Shopping(self.driver)
    def my_page_obj(self):
        return my_page.My_page(self.driver)