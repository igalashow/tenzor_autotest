В этом репозитории содержится вариант решения тестового задания на позицию разработчика в тестировании.

**!!! Для успешного запуска тестов необходимо удостовериться, что путь к вебдрайверу прописан в переменной PATH (либо прописать свои пути в файле conftest.py).**

Проект разрабатывался и тестировался под ОС Windows 7HB 64bit, версии браузеров: Chrome 92.0, Firefox 91.0. В качестве тест-раннера использовался **pytest**.

Запуск тестов возможен на браузерах Chrome и Firefox. Для выбора браузера необходимо при запуске тестов указать параметр **--browser_name=chrome** либо 
**--browser_name=firefox**

Файлы проекта:

- **test_ya_search.py и test_ya_pictures.py** - реализация тестовых сценариев "Поиск в Яндексе" и "Картинки на Яндексе".
- **conftest.py** - фикстура запуска вебдрайвера.
- **pytest.ini** - регистрация маркировки тестов.
- папка **page** - реализации PageObject-объектов (**base_page.py, main_page.py, result_page.py, pictures_page.py**), **locators.py** - вынесенные локаторы.
- **УК - тестовое задание (автотестирование), 3 кат new .docx** - тестовое задание


