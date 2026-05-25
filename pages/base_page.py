from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url: str):
        self.driver.get(url)

    def find_element(self, locator):
        """Найти видимый элемент с ожиданием."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url_contains(self, substring, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(substring))

    def find_elements(self, locator):
        """Найти все элементы (без ожидания видимости)."""
        try:
            return self.driver.find_elements(*locator)
        except StaleElementReferenceException:
            return []

    def click_element(self, locator):
        """Клик по элементу с прокруткой."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def send_keys_to_element(self, locator, text):
        """Ввод текста в поле."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        """Получить текст элемента."""
        element = self.find_element(locator)
        return element.text

    def scroll_to_element(self, element):
        """Прокрутка к элементу."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_displayed(self, locator):
        """Проверить, отображается ли элемент."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_for_element_clickable(self, locator):
        """Ожидать кликабельности элемента."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_invisible(self, locator):
        """Ожидать исчезновения элемента."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def get_current_url(self):
        """Получить текущий URL."""
        return self.driver.current_url

    def wait_for_url_to_be(self, expected_url):
        """Ожидать точного URL."""
        self.wait.until(EC.url_to_be(expected_url))

    def switch_to_window(self, window_index):
        """Переключиться на окно по индексу."""
        windows = self.driver.window_handles
        if window_index < len(windows):
            self.driver.switch_to.window(windows[window_index])
