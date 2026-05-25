import pytest
import allure
from data.test_data import ORDER_DATA_SETS
from data.urls import MAIN_PAGE_URL, ORDER_PAGE_URL
from data.error_messages import ORDER_SUCCESS_MODAL_NOT_SHOWN
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.allure_labels import ALLURE_FEATURE_ORDER, ALLURE_STORY_POSITIVE


@allure.feature(ALLURE_FEATURE_ORDER)
@allure.story(ALLURE_STORY_POSITIVE)
class TestOrderFlow:
    @allure.title(
        "Оформление заказа с валидными данными: {order_data[name]} {order_data[surname]}"
    )
    @allure.description(
        "Полный сценарий оформления заказа самоката с корректными данными"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("order_data", ORDER_DATA_SETS)
    def test_order_scooter_positive(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу сервиса"):
            main_page.open_page(MAIN_PAGE_URL)

        with allure.step("Нажать кнопку 'Заказать' в шапке сайта"):
            main_page.click_order_button(position=order_data["entry_point"])

        with allure.step("Проверить, что открылась страница оформления заказа"):
            main_page.wait_for_url_to_be(ORDER_PAGE_URL)
            assert order_page.is_step1_form_displayed()

        with allure.step(
            f"Ввести личные данные: {order_data['name']} {order_data['surname']}, "
            f"тел. {order_data['phone']}, адрес: {order_data['address']}"
        ):
            order_page.fill_personal_data(
                name=order_data["name"],
                surname=order_data["surname"],
                phone=order_data["phone"],
                address=order_data["address"],
            )

        with allure.step(
            f"Выбрать станцию метро '{order_data['station']}' из выпадающего списка"
        ):
            order_page.select_station_by_name(order_data["station"])

        with allure.step("Нажать кнопку 'Дальше' для перехода к деталям заказа"):
            order_page.proceed_to_next_step()

        with allure.step(
            f"Указать детали заказа: срок аренды — {order_data['rent_period']}, "
            f"цвет — {order_data['color']}, комментарий — '{order_data['comment']}'"
        ):
            order_page.fill_order_details(
                rent_period=order_data["rent_period"],
                color=order_data["color"],
                comment=order_data["comment"],
            )

        with allure.step("Нажать кнопку 'Заказать' для подтверждения"):
            order_page.confirm_order()

        with allure.step(
            "Проверить, что появилось сообщение об успешном оформлении заказа"
        ):
            assert order_page.is_order_success(), ORDER_SUCCESS_MODAL_NOT_SHOWN
