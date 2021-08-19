from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """ Класс основной страницы """

    def should_be_pictures_link(self):
        return self.is_element_present(*MainPageLocators.PICTURES_LINK)

    def should_be_search_field(self):
        return self.is_element_present(*MainPageLocators.SEARCH_FIELD)

    def should_be_suggest(self):
        return self.is_element_present(*MainPageLocators.SUGGEST)



    def write_a_request(self, request):
        self.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(request)

    def press_search_button(self):
        self.find_element(*MainPageLocators.SEARCH_BUTTON).click()

    def go_to_pictures_link(self):
        self.go_to_link(*MainPageLocators.PICTURES_LINK)

