from selenium.webdriver.common.by import By


class TransitionLocators:
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    LOGO_SCOOTER_ALT = (By.XPATH, "//a[.//img[@alt='Scooter']]")
    LOGO_SCOOTER_IMG = (By.XPATH, "//a[descendant::img[@alt='Scooter']]")
