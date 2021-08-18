import time
import pytest
from .pages.main_page import MainPage
from .pages.pictures_page import PicturesPage


# @pytest.mark.debug
class TestPictureYandex:
    """ Картинки в яндексе """

    def test_pictures(self, browser):
        # Проверяем наличие ссылки "Картинки"
        page = MainPage(browser)
        page.open('https://yandex.ru')
        response = page.should_be_pictures_link()
        assert response[0], f'Ссылка "Картинки" не появилась за {response[1]} сек.!'

        # Проверяем, что перешли на correct_url
        correct_url = 'https://yandex.ru/images/'
        page.go_to_pictures_link()
        pictures_page = PicturesPage(browser)
        pictures_page.swith_to_new_window()
        time.sleep(3)
        current_link = pictures_page.should_be_correct_link()
        assert correct_url in current_link , f'Адрес страницы не соответствует {correct_url}!'

        # Проверяем, что перешли в корректную категорию
        category_name = pictures_page.get_category_name()
        pictures_page.go_to_first_category_link()
        time.sleep(3)
        assert category_name in pictures_page.should_be_correct_category_name(), 'Открыта неверная категория!'

        # Проверяем, что кнопка "Вперед" работает, картинка изменяется
        pictures_page.go_to_first_pucture_from_category()
        time.sleep(3)
        prev_picture = pictures_page.get_picture_link()
        pictures_page.go_to_next_picture()
        next_picture = pictures_page.get_picture_link()
        assert prev_picture != next_picture, 'При нажатии кнопки "Вперед" картинка не изменилась!'

        # Проверяем, что кнопка "Назад" работает, возвращается предыдущая картинка
        time.sleep(3)
        pictures_page.go_to_prev_picture()
        new_prev_pictures = pictures_page.get_picture_link()
        time.sleep(3)
        assert prev_picture == new_prev_pictures, 'При нажатии кнопки "Назад" предыдущая картинка не вернулась'