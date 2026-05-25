from selenium.webdriver.common.by import By


class OrderFormLocators:
    FORM_HEADER_STEP1 = (By.CLASS_NAME, "Order_Header__BZXOb")

    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_DROPDOWN = (By.CSS_SELECTOR, "input.select-search__input")
    STATION_KRASNOSELSKAYA = (By.CSS_SELECTOR, 'li[data-value="5"]')
    STATION_KOMSOMOLSKAYA = (By.CSS_SELECTOR, 'li[data-value="6"]')

    PHONE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (
        By.CSS_SELECTOR,
        "div.Order_NextButton__1_rCA button.Button_Button__ra12g",
    )
    ERROR_MESSAGE = (By.CLASS_NAME, "Input_ErrorMessage__3HvIb")
    FORM_HEADER_STEP2 = (By.CLASS_NAME, "Order_Header__BZXOb")
    DATE_PICKER = (
        By.CSS_SELECTOR,
        "div.react-datepicker__input-container input[placeholder='* Когда привезти самокат']",
    )

    RENT_PERIOD_SELECT = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTIONS = (By.CSS_SELECTOR, "div.Dropdown-option")
    RENT_OPTION_BY_TEXT = (
        By.XPATH,
        "//div[@class='Dropdown-option' and normalize-space(text())='{}']",
    )

    COLOR_BLACK = (By.CSS_SELECTOR, 'label[for="black"]')
    COLOR_GREY = (By.CSS_SELECTOR, 'label[for="grey"]')
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.CSS_SELECTOR, "button.Button_Inverted__3IF-i")
    ORDER_BUTTON = (
        By.CSS_SELECTOR,
        "button.Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)",
    )

    @staticmethod
    def DAY_IN_CALENDAR(day):
        """
        Возвращает локатор для дня в календаре по числу.

        Args:
            day (str): число дня (например, "25")

        Returns:
            tuple: локатор (By, XPath)
        """
        return (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') "
            f"and text()='{day}' "
            f"and not(contains(@class, 'outside-month')) "
            f"and not(contains(@aria-disabled, 'true'))]",
        )

    # Дополнительные локаторы для календаря (для надёжности)
    CALENDAR_MONTH = (By.CLASS_NAME, "react-datepicker__month")
    CALENDAR_HEADER = (By.CLASS_NAME, "react-datepicker__current-month")
    CALENDAR_CONTAINER = (By.CLASS_NAME, "react-datepicker")


class ConfirmationModalLocators:
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    CONFIRM_NO_BUTTON = (
        By.CSS_SELECTOR,
        "button.Button_Button__ra12g.Button_Middle__1CSJM.Button_Inverted__3IF-i",
    )
    CONFIRM_YES_BUTTON = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ']/following-sibling::div[@class='Order_Buttons__1xGrp']//button[text()='Да']",
    )

    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[text()='Заказ оформлен']")
