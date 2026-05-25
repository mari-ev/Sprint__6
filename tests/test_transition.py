import pytest
import allure
from data.allure_labels import ALLURE_FEATURE_TRANSITIONS, ALLURE_STORY_UI_ELEMENTS
from data.urls import MAIN_PAGE_URL, ORDER_PAGE_URL
from data.error_messages import YANDEX_LOGO_TAB_NOT_OPENED
from pages.transition_page import TransitionPage


@allure.feature(ALLURE_FEATURE_TRANSITIONS)
@allure.story(ALLURE_STORY_UI_ELEMENTS)
class TestTransitions:
    @allure.title("Переход по логотипу самоката")
    @allure.description(
        "Проверяет переход на главную страницу при клике по логотипу самоката в шапке сайта"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_transition(self, driver):
        transition_page = TransitionPage(driver)

        with allure.step("Открыть страницу оформления заказа"):
            transition_page.open_page(ORDER_PAGE_URL)

        with allure.step("Кликнуть на логотип самоката в шапке страницы"):
            transition_page.click_scooter_logo()

        with allure.step("Дождаться загрузки главной страницы сервиса"):
            transition_page.wait_for_url_to_be(MAIN_PAGE_URL)

    @allure.title("Открытие Яндекс в новой вкладке")
    @allure.description(
        "Проверяет открытие сайта Яндекса в новой вкладке при клике по логотипу Яндекс"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_opens_new_tab(self, driver):
        transition_page = TransitionPage(driver)

        with allure.step("Открыть главную страницу сервиса"):
            transition_page.open_page(MAIN_PAGE_URL)

        with allure.step("Кликнуть на логотип Яндекс в шапке сайта"):
            transition_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку с сайтом Яндекса"):
            transition_page.switch_to_new_window()

        with allure.step(
            "Убедиться, что открылась страница Яндекса (содержит 'ya.ru')"
        ):
            current_url = transition_page.get_current_url()
            assert "ya.ru" in current_url, YANDEX_LOGO_TAB_NOT_OPENED
