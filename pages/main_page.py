from selenium.webdriver.common.by import By # Подключаем инструмент для поиска элементов на странице
from pages.base_page import BasePage # Подключаем базовый класс, чтобы использовать его методы

class MainPage(BasePage): # Создаем класс главной страницы и берем за основу BasePage
    
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']") # локатор верхней кнопки "Заказать"
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']") # локатор нижней кнопки "Заказать"

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']") # локатор логотипа "Самокат"
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']") # локатор логотипа "Яндекс"

    @staticmethod # Указываем, что этот метод работает сам по себе
    def get_faq_question_locator(index): # Функция, которая собирает адрес вопроса по его номеру
        return (By.ID, f"accordion__heading-{index}") # Возвращает готовый адрес вопроса с нужным номером

    @staticmethod # Тоже самостоятельный метод
    def get_faq_answer_locator(index): # Функция, которая собирает адрес ответа по его номеру
        return (By.ID, f"accordion__panel-{index}") # Возвращает готовый адрес ответа с нужным номером

    def click_header_order_button(self): # нажимаем на верхнюю кнопку заказа
        self.click_element(self.HEADER_ORDER_BUTTON) # Кликаем по верхней кнопке

    def click_footer_order_button(self): # нажимаем на нижнюю кнопку заказа
        footer_btn = self.find_element_with_wait(self.FOOTER_ORDER_BUTTON) # Ищем нижнюю кнопку
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_btn) # Прокручиваем экран до нижней кнопки
        self.click_element(self.FOOTER_ORDER_BUTTON) # Кликаем по нижней кнопке

    def click_scooter_logo(self): # нажимаем на логотип "Самокат"
        self.click_element(self.SCOOTER_LOGO) # Кликаем по логотипу Самоката

    def click_yandex_logo(self): # нажимаем на логотип "Яндекс"
        self.click_element(self.YANDEX_LOGO) # Кликаем по логотипу Яндекса

    def click_faq_question(self, index): # кликаем на вопрос из списка по его номеру
        question_element = self.find_element_with_wait(self.get_faq_question_locator(index)) # Находим нужный вопрос
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element) # Прокручиваем к центру
        self.driver.execute_script("arguments[0].click();", question_element) # Кликаем через JavaScript, чтобы исключить любые перекрытия картинкой или шапкой

    def get_faq_answer_text(self, index): # блок с текстом ответа
        answer_element = self.find_element_with_wait(self.get_faq_answer_locator(index)) # Находим блок с текстом ответа
        return answer_element.text # Возвращаем текст 