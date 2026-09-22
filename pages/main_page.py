from pages.base_page import BasePage  # Подключаем базовый класс
from locators import MainPageLocators  # Подключаем локаторы главной страницы

class MainPage(BasePage):  # Класс главной страницы, наследуется от BasePage

    def click_header_order_button(self):  # Метод для нажатия на верхнюю кнопку "Заказать"
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    def click_footer_order_button(self):  # Метод для нажатия на нижнюю кнопку "Заказать"
        self.scroll_to_element(MainPageLocators.FOOTER_ORDER_BUTTON)  # Прокручиваем до нижней кнопки
        self.click_element(MainPageLocators.FOOTER_ORDER_BUTTON)

    def click_scooter_logo(self):  # Метод для клика по логотипу "Самокат"
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):  # Метод для клика по логотипу "Яндекс"
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_faq_question(self, index):  # Метод для клика на вопрос FAQ по его номеру
        question_locator = MainPageLocators.get_faq_question_locator(index)
        self.scroll_to_element_center(question_locator)  # Прокручиваем к центру экрана
        self.click_element_with_js(question_locator)  # Кликаем через JS

    def get_faq_answer_text(self, index):  # Метод для получения текста ответа FAQ
        answer_locator = MainPageLocators.get_faq_answer_locator(index)
        return self.get_text_from_element(answer_locator)