from pages.base_page import BasePage
from locators.order_locators import OrderFormLocators, ConfirmationModalLocators
from datetime import datetime, timedelta
from data.mapping_data import COLOR_MAPPING, STATION_MAPPING
from data.error_messages import UNKNOWN_STATION_ERROR, UNKNOWN_COLOR_ERROR
from data.default_params import DEFAULT_RENT_PERIOD, DEFAULT_COLOR
from data.text_constants import SUCCESS_MODAL_EXPECTED_TEXT
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OrderPage(BasePage):
    def is_step1_form_displayed(self):
        return self.is_element_displayed(OrderFormLocators.FORM_HEADER_STEP1)

    def fill_personal_data(self, name, surname, phone, address):
        self.send_keys_to_element(OrderFormLocators.NAME_FIELD, name)
        self.send_keys_to_element(OrderFormLocators.SURNAME_FIELD, surname)
        self.send_keys_to_element(OrderFormLocators.PHONE_FIELD, phone)
        self.send_keys_to_element(OrderFormLocators.ADDRESS_FIELD, address)

    def select_station_by_name(self, station_name):
        if station_name not in STATION_MAPPING:
            raise ValueError(UNKNOWN_STATION_ERROR.format(station_name))
        station_input = self.find_element(OrderFormLocators.STATION_DROPDOWN)
        station_input.click()
        locator_name = STATION_MAPPING[station_name]
        station_locator = getattr(OrderFormLocators, locator_name)
        self.click_element(station_locator)

    def proceed_to_next_step(self):
        self.click_element(OrderFormLocators.NEXT_BUTTON)

    def select_date(self, days_from_today=1):
        date_picker = self.find_element(OrderFormLocators.DATE_PICKER)
        date_picker.click()

        today = datetime.now()
        target_day = (today + timedelta(days=days_from_today)).day
        day_locator = OrderFormLocators.DAY_IN_CALENDAR(str(target_day))
        day_element = self.wait_for_element_clickable(day_locator)
        day_element.click()

    def select_rent_period(self, rent_period):
        self.click_element(OrderFormLocators.RENT_PERIOD_SELECT)
        self.wait.until(
            EC.visibility_of_all_elements_located(OrderFormLocators.RENT_OPTIONS)
        )

        rent_option_locator = (
            OrderFormLocators.RENT_OPTION_BY_TEXT[0],
            OrderFormLocators.RENT_OPTION_BY_TEXT[1].format(rent_period),
        )
        self.click_element(rent_option_locator)

    def select_color(self, color="black"):
        if color not in COLOR_MAPPING:
            raise ValueError(UNKNOWN_COLOR_ERROR.format(color))
        color_locator_name = COLOR_MAPPING[color]
        color_locator = getattr(OrderFormLocators, color_locator_name)
        self.click_element(color_locator)

    def add_comment(self, comment=""):
        if comment:
            self.send_keys_to_element(OrderFormLocators.COMMENT_FIELD, comment)

    def place_order(self):
        self.click_element(OrderFormLocators.ORDER_BUTTON)
        self.wait_for_element_visible(ConfirmationModalLocators.CONFIRMATION_MODAL)

    def fill_order_details(
        self, rent_period, color="black", comment="", days_from_today=1
    ):
        self.select_date(days_from_today)
        self.select_rent_period(rent_period)
        self.select_color(color)
        self.add_comment(comment)
        self.place_order()

    def confirm_order(self):
        self.wait_for_element_visible(ConfirmationModalLocators.CONFIRMATION_MODAL)
        self.click_element(ConfirmationModalLocators.CONFIRM_YES_BUTTON)

    def is_order_success(self):
        if not self.is_element_displayed(
            ConfirmationModalLocators.SUCCESS_MODAL_HEADER
        ):
            return False
        element = self.find_element(ConfirmationModalLocators.SUCCESS_MODAL_HEADER)
        return SUCCESS_MODAL_EXPECTED_TEXT in element.text
