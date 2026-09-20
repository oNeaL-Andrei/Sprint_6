from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver # Сохраняем экземпляр драйвера браузера, чтобы он был доступен во всех дочерних классах

    def find_element_with_wait(self, locator): # Метод для поиска элемента с явным ожиданием видимости
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)) # Ждем до 10 секунд, пока элемент появится на странице, и возвращаем его

    def click_element(self, locator): # Универсальный метод клика с ожиданием кликабельности
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)) # Ждем, пока элемент станет кликабельным
        element.click() # Кликаем по нему