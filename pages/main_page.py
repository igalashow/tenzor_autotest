from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """ Класс основной страницы """

    def should_be_search_field(self):
        return self.is_element_present(*MainPageLocators.SEARCH_FIELD)

    def should_be_suggest(self):
        return self.is_element_present(*MainPageLocators.SUGGEST)

    def write_a_request(self, request):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(request)

    def press_search_button(self):
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()