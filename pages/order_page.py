from selenium.webdriver.common.by import By # Подключаем инструмент для поиска элементов на странице
from selenium.webdriver.common.keys import Keys # Подключаем класс для отправки специальных клавиш клавиатуры 
from pages.base_page import BasePage # Подключаем базовый класс

class OrderPage(BasePage): # Создаем класс страницы заказа на основе BasePage
    
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") # поля ввода имени
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']") # поля ввода фамилии
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поля ввода адреса
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']") # поля выбора станции метро
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поля ввода телефона
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[text()='Далее']") # кнопки "Далее"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поля выбора даты
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder") # выпадающего списка срока аренды
    COLOR_BLACK_CHECKBOX = (By.XPATH, "//label[text()='чёрный жемчуг']/input") # чекбокса черного цвета
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # комментария для курьера
    FINISH_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']") # кнопка "Заказать" на втором шаге
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']") # кнопка "Да" подтверждения
    SUCCESS_POPUP = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]") # всплывающее окно успешного заказа

    # Работа с формой заказа 

    def set_first_name(self, first_name): # заполняем поле "Имя"
        self.find_element_with_wait(self.FIRST_NAME_INPUT).send_keys(first_name) # Находим поле имени вводим переданное значение 

    def set_last_name(self, last_name): # заполняем поле "фамилия"
        self.find_element_with_wait(self.LAST_NAME_INPUT).send_keys(last_name) # Находим поле фамилии вводим переданное значение

    def set_address(self, address): # заполняем поле "адрес"
        self.find_element_with_wait(self.ADDRESS_INPUT).send_keys(address) # Находим поле адреса вводим переданное значение

    def set_metro(self, metro_station): # выбираем санцию метро
        metro_field = self.find_element_with_wait(self.METRO_INPUT)
        metro_field.click() # Находим поле ввода метро и кликаем на него, чтобы открыть список
        metro_field.send_keys(metro_station) # Вводим название станции метро
        station_option = (By.XPATH, f"//div[text()='{metro_station}']") # Формируем динамический локатор для выбора нужной станции из выпадающего списка      
        self.find_element_with_wait(station_option).click() # Находим появившуюся станцию в списке кликаем по ней

    def set_phone(self, phone): # заполняем поле телефон
        self.find_element_with_wait(self.PHONE_INPUT).send_keys(phone) # Находим поле телефона вводим переданное значение

    def click_next_button(self): # нажимаем кнопку "далее"
        self.find_element_with_wait(self.NEXT_BUTTON).click()

    def fill_personal_info(self, first_name, last_name, address, metro, phone): # заполняем поля формы заказа
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button() # Нажимаем кнопку перехода далее

    def set_date(self, date): # заполняем дату доставки
        date_field = self.find_element_with_wait(self.DATE_INPUT) # Находим поле даты с ожиданиями
        date_field.send_keys(date)  # Вводим значение даты
        date_field.send_keys(Keys.ENTER) # Нажимаем клавишу ENTER, чтобы закрыть всплывающий календарь

    def set_rental_period(self, period_text): # выбираем срок аренды из выподающего списка
        self.find_element_with_wait(self.RENTAL_PERIOD_DROPDOWN).click() # Кликаем по выпадающему списку срока аренды
        period_option = (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{period_text}']") # создаём локатор для выбора времени аренды
        self.find_element_with_wait(period_option).click() # Находим нужный срок аренды кликаем по нему

    def select_black_color(self):  # выбор черного цвета самоката
        self.find_element_with_wait(self.COLOR_BLACK_CHECKBOX).click() # Находим чекбокс черного цвета кликаем по нему

    def set_comment(self, comment): # поле коментария для курьера
        self.find_element_with_wait(self.COMMENT_INPUT).send_keys(comment) # Находим поле комментария вводим текст

    def click_finish_order_button(self): # нажимаем кнопку "заказать" 
        self.find_element_with_wait(self.FINISH_ORDER_BUTTON).click() # Находим кнопку заказа кликаем по ней

    def confirm_order(self): # подтверждения заказа во всплывающем окне (нажатие кнопки "Да")
        self.find_element_with_wait(self.CONFIRM_YES_BUTTON).click() # Находим кнопку "Да" кликаем

    def fill_rental_info(self, date, period_text, comment): # заполняем поля второго шага формы заказа
        self.set_date(date) # поле даты доставки        
        self.set_rental_period(period_text) # срок аренды
        self.select_black_color() # выбираем цвет самоката
        self.set_comment(comment) # вводим комментарий для курьера
        self.click_finish_order_button() # Нажимаем кнопку "Заказать"
        self.confirm_order() # Подтверждаем заказ во всплывающем окне

    def check_success_popup_is_displayed(self): # проверяем что появилось окно успешного оформления заказа
        return self.find_element_with_wait(self.SUCCESS_POPUP).is_displayed() # Возвращаем результат проверки видимости всплывающего окна