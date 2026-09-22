from selenium.webdriver.support.ui import WebDriverWait # Подключаем инструмент для явных ожиданий
from selenium.webdriver.support import expected_conditions as EC # Подключаем готовые условия ожидания
from selenium.webdriver.common.keys import Keys # Подключаем класс для отправки клавиш клавиатуры

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver # Сохраняем экземпляр драйвера браузера для всех классов

    def find_element_with_wait(self, locator): # Метод для поиска элемента с явным ожиданием видимости
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)) # Ждем до 10 секунд, пока элемент появится на странице

    def click_element(self, locator): # Универсальный метод клика с ожиданием кликабельности
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)) # Ждем, пока элемент станет кликабельным
        element.click() # Кликаем по элементу

    def send_keys_to_element(self, locator, text): # Метод для ввода текста в элемент
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        element.send_keys(text) # Вводим переданное значение

    def send_keys_and_press_enter(self, locator, text): # Метод для ввода текста и нажатия клавиши Enter
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        element.send_keys(text) # Вводим значение
        element.send_keys(Keys.ENTER) # Нажимаем клавишу Enter

    def get_text_from_element(self, locator): # Метод для получения текста из элемента
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        return element.text # Возвращаем текст элемента

    def is_element_displayed(self, locator): # Метод для проверки отображения элемента на странице
        return self.find_element_with_wait(locator).is_displayed() # Возвращаем True, если элемент виден

    def scroll_to_element(self, locator): # Метод для прокрутки экрана к элементу
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем страницу до элемента

    def scroll_to_element_center(self, locator): # Метод для прокрутки элемента в центр экрана
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element) # Прокручиваем к центру

    def click_element_with_js(self, locator): # Метод для клика по элементу с помощью JavaScript
        element = self.find_element_with_wait(locator) # Находим элемент с ожиданием
        self.driver.execute_script("arguments[0].click();", element) # Кликаем по элементу через JS

    def get_current_url(self): # Метод для получения текущего URL страницы
        return self.driver.current_url # Возвращает адрес текущей страницы

    def wait_for_new_window_and_switch(self): # Метод для ожидания открытия новой вкладки и переключения на нее
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1) # Ждем появление второй вкладки
        self.driver.switch_to.window(self.driver.window_handles[1]) # Переключаем фокус драйвера на новую вкладку

    def wait_for_url_contains(self, url_part): # Метод для ожидания появления части URL в адресе страницы
        return WebDriverWait(self.driver, 10).until(EC.url_contains(url_part)) # Ждем, пока в URL появится указаная часть