from selenium.webdriver.common.by import By # Подключаем инструмент для способов поиска элементов на странице

class MainPageLocators: # Класс для локаторов главной страницы
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']") # Локатор верхней кнопки "Заказать"
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']") # Локатор нижней кнопки "Заказать"

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']") # Локатор логотипа "Самокат"
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']") # Локатор логотипа "Яндекс"

    @staticmethod # Статический метод для формирования динамического локатора вопроса FAQ
    def get_faq_question_locator(index): # Принимает индекс вопроса (0-7)
        return (By.ID, f"accordion__heading-{index}") # Возвращает кортеж с вычисленным ID вопроса

    @staticmethod # Статический метод для формирования динамического локатора ответа FAQ
    def get_faq_answer_locator(index): # Принимает индекс ответа (0-7)
        return (By.ID, f"accordion__panel-{index}") # Возвращает кортеж с вычисленным ID ответа

class OrderPageLocators: # Класс для локаторов страницы заказа
    # Персональные данные
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") # Поле ввода имени
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']") # Поле ввода фамилии
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Поле ввода адреса
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']") # Поле выбора станции метро
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле ввода телефона
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[text()='Далее']") # Кнопка "Далее"

    # Аренда самоката
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Поле выбора даты
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder") # Выпадающий список срока аренды
    COLOR_BLACK_CHECKBOX = (By.XPATH, "//label[text()='чёрный жемчуг']/input") # Чекбокс черного цвета
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Поле комментария
    FINISH_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']") # Кнопка "Заказать" на 2 шаге
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']") # Кнопка "Да" в всплывающем окне
    SUCCESS_POPUP = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]") # Окно успешного заказа

    @staticmethod # Статический метод для динамического выбора станции метро
    def get_metro_station_locator(station_name): # Принимает название станции
        return (By.XPATH, f"//div[text()='{station_name}']") # Возвращает локатор элемента нужной станции в списке

    @staticmethod # Статический метод для динамического выбора срока аренды
    def get_rental_period_option_locator(period_text): # Принимает текст периода (например, "сутки")
        return (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{period_text}']") # Возвращает локатор нужного элемента в списке