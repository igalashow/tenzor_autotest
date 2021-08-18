from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    """ Класс базовой страницы """

    def __init__(self, browser):
        """ Конструктор, вызывающий браузер """
        self.browser = browser

    def open(self, url):
        """ Открывает страницу в браузере """
        self.browser.get(url)

    def is_element_present(self, how, what, timeout=10):
        """ Проверяет наличие элемента (загрузка за время timeout) """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return (False, timeout)
        return (True, '')

