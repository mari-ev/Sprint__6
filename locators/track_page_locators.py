from selenium.webdriver.common.by import By


class TrackPageLocators:
    # Поле ввода номера заказа — по классу (наиболее стабильный вариант)
    TRACK_NUMBER_INPUT = (By.CLASS_NAME, "Track_Input__1g7lq")

    # Кнопка поиска заказа — по тексту (если текст стабилен)
    TRACK_SEARCH_BUTTON = (By.XPATH, "//button[text()='Посмотреть']")

    # Блок информации о заказе — основной контейнер
    ORDER_INFO = (By.CLASS_NAME, "Track_OrderInfo__2fpDL")

    # Поля информации — через sibling (заголовок → значение)
    CUSTOMER_NAME = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Имя']/following-sibling::div",
    )
    CUSTOMER_SURNAME = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Фамилия']/following-sibling::div",
    )
    DELIVERY_ADDRESS = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Адрес']/following-sibling::div",
    )
    METRO_STATION = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Станция метро']/following-sibling::div",
    )
    PHONE_NUMBER = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Телефон']/following-sibling::div",
    )
    DELIVERY_DATE = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Дата доставки']/following-sibling::div",
    )
    RENT_PERIOD = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Срок аренды']/following-sibling::div",
    )
    SCOOTER_COLOR = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Цвет']/following-sibling::div",
    )

    # Статус заказа (если отображается)
    ORDER_STATUS = (
        By.XPATH,
        "//div[@class='Track_Title__1XfhB' and text()='Статус']/following-sibling::div",
    )

    # Кнопка отмены заказа — если доступна
    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text()='Отменить заказ']")

    # Сообщение «Заказ не найден» (для негативного сценария)
    ORDER_NOT_FOUND_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ не найден')]")

    # Сообщение «Введите номер заказа» (для валидации)
    ENTER_ORDER_NUMBER_MESSAGE = (
        By.XPATH,
        "//div[contains(text(), 'Введите номер заказа')]",
    )
