from .base_page import BasePage
from .locators import ResultPageLocators


class ResultPage(BasePage):
    """ Класс страницы результатов поиска """

    def should_be_result_table(self):
        return self.is_element_present(*ResultPageLocators.SEARCH_RESULT)

