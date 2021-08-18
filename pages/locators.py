from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='text']")
    SUGGEST = (By.CSS_SELECTOR, '.mini-suggest__popup-content')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    PICTURES_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')


class ResultPageLocators:
    SEARCH_RESULT = (By.CSS_SELECTOR, 'ul#search-result')
    LINKS = (By.CSS_SELECTOR, 'h2 > a')


class PicturesPageLocators:
    FIRST_CATEGORY = (By.XPATH, '//div[@class="PopularRequestList"]//a')
    CATEGORY_NAME = (By.CSS_SELECTOR, 'input.input__control')
    FIRST_PICTURE_FROM_CATEGORY = (By.XPATH, "//div[@class='serp-controller__content']//a")
    PICTURE_LINK = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_next')
    PREV_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_prev')

