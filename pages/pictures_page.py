from .base_page import BasePage


class PicturesPage(BasePage):

    def should_be_correct_link(self):
        return self.browser.current_url

    def swith_to_new_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
