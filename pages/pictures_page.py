from .base_page import BasePage
from .locators import PicturesPageLocators


class PicturesPage(BasePage):

    def should_be_correct_link(self):
        return self.browser.current_url

    def should_be_correct_category_name(self):
        return self.browser.find_element(*PicturesPageLocators.CATEGORY_NAME).get_attribute('value')

    def swith_to_new_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def go_to_first_category_link(self):
        self.go_to_link(*PicturesPageLocators.FIRST_CATEGORY)

    def get_category_name(self):
        category_name = self.browser.find_element(*PicturesPageLocators.FIRST_CATEGORY).text
        return category_name
