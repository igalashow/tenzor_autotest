import time

from .base_page import BasePage
from .locators import ResultPageLocators


class ResultPage(BasePage):
    """ Класс страницы результатов поиска """

    def should_be_result_table(self):
        return self.is_element_present(*ResultPageLocators.SEARCH_RESULT)

    def should_be_in_top5(self, links, keywrd):
        # Зачистка от рекламы яндекса
        for index, link in enumerate(links):
            if 'yabs.yandex.ru' in link:
                links.remove(link)
                links.insert(index, ' ')
        # Проверка на тор5
        for link in links[:5]:
            if keywrd in link:
                return True
        return False

    def get_results(self):
        a_tags = self.find_elements(*ResultPageLocators.LINKS)
        links = []
        for a in a_tags:
            links.append(a.get_attribute('href'))
            time.sleep(0.1)
        return links
