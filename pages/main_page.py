from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data.urls import MAIN_PAGE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = MAIN_PAGE_URL

    def open(self):
        """Открыть главную страницу."""
        self.driver.get(self.base_url)

    def close_cookie_banner(self):
        """Закрыть баннер с куки, если он есть."""
        if self.is_element_displayed(MainPageLocators.COOKIE_BANNER):
            self.click_element(MainPageLocators.COOKIE_BUTTON)

    def click_order_button(self, position="top"):
        """Кликнуть на кнопку «Заказать» вверху или внизу страницы."""
        self.close_cookie_banner()
        locator = (
            MainPageLocators.ORDER_BUTTON_TOP
            if position == "top"
            else MainPageLocators.ORDER_BUTTON_BOTTOM
        )
        self.click_element(locator)

    def scroll_to_faq(self):
        """Прокрутить к секции FAQ."""
        faq_section = self.find_element(MainPageLocators.FAQ_SECTION)
        self.scroll_to_element(faq_section)

    def open_faq_question(self, index):
        """Открыть вопрос FAQ по индексу (1–8)."""
        question_button = self.wait_for_element_clickable(
            MainPageLocators.FAQ_QUESTION_BUTTON(index)
        )
        self.scroll_to_element(question_button)
        question_button.click()
        # Ждём появления панели ответа после клика
        self.wait_for_element_visible(MainPageLocators.FAQ_ANSWER_PANEL(index))

    def is_faq_answer_visible(self, index):
        """Проверить, виден ли ответ на вопрос FAQ."""
        elements = self.find_elements(MainPageLocators.FAQ_ANSWER_PANEL(index))
        return bool(elements) and elements[0].is_displayed()

    def get_faq_answer_text(self, index):
        """Получить текст ответа на вопрос FAQ."""
        elements = self.find_elements(MainPageLocators.FAQ_ANSWER_TEXT(index))
        return elements[0].text if elements else ""
