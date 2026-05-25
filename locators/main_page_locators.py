from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(., 'Заказать')])[last()]")
    FAQ_SECTION = (By.CLASS_NAME, "accordion")

    @staticmethod
    def FAQ_QUESTION_BUTTON(index):
        return (
            By.CSS_SELECTOR,
            f"div[data-accordion-component='AccordionItem']:nth-of-type({index + 1}) "
            f"div[data-accordion-component='AccordionItemButton']",
        )

    @staticmethod
    def FAQ_ANSWER_PANEL(index):
        return (
            By.CSS_SELECTOR,
            f"div[data-accordion-component='AccordionItem']:nth-of-type({index + 1}) "
            f"div[data-accordion-component='AccordionItemPanel']",
        )

    @staticmethod
    def FAQ_ANSWER_TEXT(index):
        return (
            By.CSS_SELECTOR,
            f"div[data-accordion-component='AccordionItem']:nth-of-type({index + 1}) "
            f"div[data-accordion-component='AccordionItemPanel'] p",
        )
