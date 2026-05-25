import pytest
import allure
from pages.main_page import MainPage
from data.allure_labels import ALLURE_FEATURE_FAQ, ALLURE_STORY_UI_ELEMENTS
from data.test_params import FAQ_QUESTION_INDICES, FAQ_QUESTION_IDS
from data.error_messages import FAQ_ANSWER_NOT_OPENED


@allure.feature(ALLURE_FEATURE_FAQ)
@allure.story(ALLURE_STORY_UI_ELEMENTS)
@pytest.mark.parametrize("question_index", FAQ_QUESTION_INDICES, ids=FAQ_QUESTION_IDS)
@allure.title("FAQ: открыть вопрос №{question_index}")
@allure.description(
    "Проверяет, что при клике на вопрос FAQ открывается соответствующий ответ"
)
@allure.severity(allure.severity_level.NORMAL)
def test_faq_questions_open(driver, question_index):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу сервиса"):
        page.open()

    with allure.step("Закрыть баннер с уведомлением о куки, если он есть"):
        page.close_cookie_banner()

    with allure.step("Прокрутить страницу вниз до раздела 'Часто задаваемые вопросы'"):
        page.scroll_to_faq()

    with allure.step(f"Кликнуть на вопрос №{question_index + 1} в разделе FAQ"):
        page.open_faq_question(question_index)

    with allure.step(
        f"Проверить, что ответ на вопрос №{question_index + 1} открылся и виден на экране"
    ):
        assert page.is_faq_answer_visible(question_index), FAQ_ANSWER_NOT_OPENED.format(
            question_index + 1
        )
