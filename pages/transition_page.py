from pages.base_page import BasePage
from locators.transition_locators import TransitionLocators


class TransitionPage(BasePage):
    def click_yandex_logo(self):
        self.click_element(TransitionLocators.LOGO_YANDEX)

    def click_scooter_logo(self):
        self.click_element(TransitionLocators.LOGO_SCOOTER)

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.wait_for_url_contains("ya.ru")
