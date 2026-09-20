import pytest  # Подключаем фреймворк pytest для запуска тестов
from selenium.webdriver.support.ui import WebDriverWait  # Подключаем класс WebDriverWait для настройки ожиданий
from pages.main_page import MainPage  # Импортируем класс главной страницы
from pages.order_page import OrderPage  # Импортируем класс страницы заказа

class TestOrderAndNavigation:  # Объявляем класс для группировки тестов заказа и навигации

    # Создаем список с двумя разными наборами данных для параметризации
    order_data = [
        ("Иван", "Иванов", "Москва, ул. Арбат, 1", "Черкизовская", "+79991112233", "01.10.2026", "сутки", "Комментарий: позвонить за час"),
        ("Анна", "Смирнова", "Москва, пр. Мира, 10", "Сокольники", "+79998887766", "02.10.2026", "двое суток", "Домофон не работает")
    ]

    # Двойная параметризация: передаем данные теста, и точку входа в сценарий заказа (верхняя или нижняя кнопка)
    @pytest.mark.parametrize("name, last_name, address, metro, phone, date, period, comment", order_data)  # Декоратор для запуска теста с разными данными
    @pytest.mark.parametrize("order_button", ["top", "bottom"], ids=["top_button", "bottom_button"])  # Параметризируем точку входа в сценарий заказа
    def test_order_positive_flow(self, driver, name, last_name, address, metro, phone, date, period, comment, order_button):  # Единый тест заказа для любой точки входа
        main_page = MainPage(driver)  # Создаем объект главной страницы

        if order_button == "top":  # Проверяем, какая точка входа выбрана
            main_page.click_header_order_button()  # Кликаем по верхней кнопке "Заказать"
        else:
            main_page.click_footer_order_button()  # Прокручиваем страницу вниз и кликаем по нижней кнопке "Заказать"

        order_page = OrderPage(driver)  # Создаем объект страницы заказа
        order_page.fill_personal_info(name, last_name, address, metro, phone)  # Заполняем форму личными данными 
        order_page.fill_rental_info(date, period, comment)  # Заполняем данные об аренде самоката и подтверждаем заказ
        assert order_page.check_success_popup_is_displayed()  # Проверяем, что появилось всплывающее окно об успешном создании заказа

    def test_logo_scooter_redirect_to_main(self, driver):  # Тест клика по логотипу "самокат"
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_header_order_button()  # Переходим на страницу заказа, чтобы оказаться не на главной

        main_page.click_scooter_logo()  # Кликаем по логотипу "самокат" в шапке
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"  # Проверяем, что текущий URL совпадает с главной страницей сервиса

    def test_logo_yandex_redirect_to_dzen(self, driver):  # Тест клика по логотипу "Яндекс"
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_yandex_logo()  # Кликаем по логотипу "Яндекс" в шапке сайта

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)  # Ожидаем появления второй вкладки в браузере перед переключением
        driver.switch_to.window(driver.window_handles[1])  # Переключаем фокус драйвера на новую открывшуюся вкладку браузера
        WebDriverWait(driver, 10).until(lambda d: "about:blank" not in d.current_url)  # Ожидаем, пока страница Дзена прогрузится и URL перестанет быть пустым (about:blank)
        assert "dzen.ru" in driver.current_url  # Проверяем, что в открывшемся адресе новой вкладки есть домен Дзена