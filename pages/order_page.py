from pages.base_page import BasePage  # Импортируем базовый класс страниц
from locators import OrderPageLocators  # Импортируем локаторы страницы заказа

class OrderPage(BasePage):  # Класс для работы со страницей оформления заказа

    def set_first_name(self, name):  # Метод для ввода имени
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_INPUT, name)

    def set_last_name(self, last_name):  # Метод для ввода фамилии
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)

    def set_address(self, address):  # Метод для ввода адреса
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    def set_metro(self, metro_station):  # Метод для выбора станции метро из списка
        self.click_element(OrderPageLocators.METRO_INPUT)  # Кликаем по полю ввода метро
        self.send_keys_to_element(OrderPageLocators.METRO_INPUT, metro_station)  # Вводим название станции
        metro_option_locator = OrderPageLocators.get_metro_station_locator(metro_station)  # Получаем локатор нужной станции
        self.click_element(metro_option_locator)  # Кликаем по найденной станции в выпадающем списке

    def set_phone(self, phone):  # Метод для ввода номера телефона
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)

    def click_next_button(self):  # Метод для нажатия кнопки "Далее"
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)  # Прокручиваем страницу до кнопки "Далее"
        self.click_element(OrderPageLocators.NEXT_BUTTON)  # Кликаем "Далее"

    def fill_personal_info(self, name, last_name, address, metro, phone):  # заполняем лмчные данные
        self.set_first_name(name)  # Заполняем поле "Имя"
        self.set_last_name(last_name)  # Заполняем поле "Фамилия"
        self.set_address(address)  # Заполняем поле "Адрес"
        self.set_metro(metro)  # Выбираем станцию метро
        self.set_phone(phone)  # Заполняем поле "Телефон"
        self.click_next_button()  # Нажимаем кнопку "Далее"

    def set_delivery_date(self, date):  # Метод для ввода даты доставки
        self.send_keys_and_press_enter(OrderPageLocators.DATE_INPUT, date)  # Вводим дату и нажимаем Enter для подтверждения календаря

    def set_rental_period(self, period):  # Метод для выбора срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)  # Открываем выпадающий список сроков аренды
        period_option_locator = OrderPageLocators.get_rental_period_option_locator(period)  # Получаем локатор с нужным периодом
        self.click_element(period_option_locator)  # Кликаем по требуемому периоду в списке

    def select_color_black(self):  # Метод для выбора черного цвета
        self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)  # Выбираем чекбокс "черный жемчуг"

    def set_comment(self, comment):  # Метод для ввода комментария
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)  # Заполняем поле комментария для курьера

    def click_finish_order_button(self):  # Метод для клика по кнопке "Заказать" 
        self.scroll_to_element(OrderPageLocators.FINISH_ORDER_BUTTON)  # Прокручиваем страницу к кнопке
        self.click_element(OrderPageLocators.FINISH_ORDER_BUTTON)  # Кликаем по кнопке создания заказа

    def click_confirm_yes_button(self):  # Метод для нажатия кнопки "Да" 
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)  # Кликаем "Да"

    def fill_rental_info(self, date, period, comment):  # заполняем данные об аренде
        self.set_delivery_date(date)  # Указываем дату
        self.set_rental_period(period)  # Указываем срок аренды
        self.select_color_black()  # выбираем цвет
        self.set_comment(comment)  # Заполняем комментарий
        self.click_finish_order_button()  # Нажимаем кнопку "Заказать"
        self.click_confirm_yes_button()  # Подтверждаем создание заказа кнопкой "Да"

    def check_success_popup_is_displayed(self):  # Метод проверки всплывающего окна об успешном оформлении
        return self.is_element_displayed(OrderPageLocators.SUCCESS_POPUP)  # Возвращает True, если всплывающее окно появилось