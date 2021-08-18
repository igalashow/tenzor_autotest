from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='text']")
    SUGGEST = (By.CSS_SELECTOR, '.mini-suggest__popup-content')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

class ResultPageLocators:
    SEARCH_RESULT = (By.CSS_SELECTOR, 'ul#search-result')