import time
import pytest
from .pages.main_page import MainPage
from .pages.result_page import ResultPage


class TestSearchFromMainPage():
    """"""

    def test_should_be_working_search_field(self, browser):
        """ Проверяет наличие поля поиска и появление таблицы с подсказками """
        url = 'https://yandex.ru'
        page = MainPage(browser)
        page.open(url)

        response = page.should_be_search_field()
        assert response[0], f'На странице {url} не появилось поле поиска за {response[1]} сек.!'

        page.write_a_request('Тензор')
        time.sleep(3)
        response = page.should_be_suggest()
        assert response[0], f'Таблица с подсказками не появилась за {response[1]} сек.!'

    def test_should_de_result_table(self, browser):
        """ Проверяет наличие таблицы результатов поиска """
        page = MainPage(browser)
        page.open('https://yandex.ru')
        page.write_a_request('Тензор')
        page.press_search_button()
        result_page = ResultPage(browser)

        response = result_page.should_be_result_table()
        assert response[0], f'Таблица результатов поиска не появилась за {response[1]} сек.!'

    @pytest.mark.debug
    def test_should_be_keyword_in_top5(self, browser):
        """ Проверяет наличие ключевого слова в первых 5 результатах поиска """
        keywrd = 'tensor.ru'
        page = MainPage(browser)
        page.open('https://yandex.ru')
        page.write_a_request('Тензор')
        page.press_search_button()
        result_page = ResultPage(browser)
        links = result_page.get_results()

        assert result_page.should_be_in_top5(links, keywrd), f'Ключевое слово {keywrd} отсутствует в первых 5 результатах'


