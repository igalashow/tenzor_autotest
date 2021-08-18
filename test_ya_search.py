import time
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
        url = 'https://yandex.ru'
        page = MainPage(browser)
        page.open(url)
        page.write_a_request('Тензор')
        page.press_search_button()
        result_page = ResultPage(browser)
        # result_page.open(browser.current_url)

        response = result_page.should_be_result_table()
        assert response[0], f'Таблица результатов поиска не появилась за {response[1]} сек.!'

