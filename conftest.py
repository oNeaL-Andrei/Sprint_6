import pytest # Подключаем инструмент pytest для создания фикстур
from selenium import webdriver # Подключаем веб-драйвер для управления браузером
from data import Urls # Импортируем URL-адреса проекта


@pytest.fixture # Объявляем фикстуру pytest, которая готовит окружение для тестов
def driver(): # Создаем функцию, которая будет запускать и закрывать браузер
    browser = webdriver.Firefox() # Запускаем браузер Firefox
    browser.get(Urls.BASE_URL) # Открываем Яндекс.Самокат
    yield browser # Передаем управление браузером тесту
    browser.quit() # Закрываем браузер после завершения теста
