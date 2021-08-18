from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    """ Класс базовой страницы """

    def __init__(self, browser, timeout=5):
        """ Конструктор, вызывающий браузер """
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        """ Открывает страницу в браузере """
        try:
            self.browser.get(url)
        except WebDriverException as e:
            raise AssertionError('WebDriverException', e)

    def go_to_link(self, *locator):
        """ Переходит по ссылке """
        self.browser.find_element(locator[0], locator[1]).click()

    def is_element_present(self, how, what, timeout=10):
        """ Проверяет наличие элемента (загрузка за время timeout) """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return (False, timeout)
        return (True, '')

