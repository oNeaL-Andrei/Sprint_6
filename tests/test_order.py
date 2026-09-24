import pytest  # Подключаем pytest
import allure  # Подключаем Allure для создания отчётов
from pages.main_page import MainPage  # Импортируем класс главной страницы
from pages.order_page import OrderPage  # Импортируем класс страницы заказа
from data import OrderData, Urls  # Импортируем тестовые данные для заказа и URL-адреса


class TestOrderAndNavigation:  # Класс для тестов заказа и навигации по логотипам

    @allure.title("Проверка оформления заказа через верхнюю кнопку")  # Добавление заголовка в отчёт Allure
    @pytest.mark.parametrize("name, last_name, address, metro, phone, date, period, comment", OrderData.ORDER_DATA_LIST)  # Параметризация по всем наборам данных для заказа
    def test_order_positive_flow(self, driver, name, last_name, address, metro, phone, date, period, comment):  # Тест полного сценария заказа через верхнюю кнопку
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_header_order_button()  # Кликаем по верхней кнопке "Заказать"

        order_page = OrderPage(driver)  # Создаем объект страницы заказа
        order_page.fill_personal_info(name, last_name, address, metro, phone)  # Заполняем Личные данные
        order_page.fill_rental_info(date, period, comment)  # Заполняем Данные об аренде
        assert order_page.check_success_popup_is_displayed()  # Проверяем, что появилось окно об успешном заказе

    @allure.title("Проверка перехода к заказу через нижнюю кнопку")  # Добавление заголовка в отчёт Allure
    def test_order_bottom_button(self, driver):  # Тест второй точки входа в сценарий заказа
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_footer_order_button()  # Прокручиваем вниз и кликаем по нижней кнопке "Заказать"

        order_page = OrderPage(driver)  # Создаем объект страницы заказа
        assert order_page.get_current_url() == Urls.ORDER_PAGE_URL  # Проверяем, что открылась страница заказа

    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")  # Добавление заголовка в отчёт Allure
    def test_logo_scooter_redirect_to_main(self, driver):  # Тест клика по логотипу "Самокат"
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_header_order_button()  # Переходим на страницу заказа, чтобы уйти с главной
        main_page.click_scooter_logo()  # Кликаем по логотипу "Самокат"
        assert main_page.get_current_url() == Urls.BASE_URL  # Проверяем что вернулись на главную страницу

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")  # Добавление заголовка в отчёт Allure
    def test_logo_yandex_redirect_to_dzen(self, driver):  # Тест клика по логотипу "Яндекс"
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_yandex_logo()  # Кликаем по логотипу "Яндекс"
        main_page.wait_for_new_window_and_switch()  # Ждем открытия новой вкладки и переключаемся на нее
        assert main_page.wait_for_url_contains(Urls.DZEN_URL)  # Проверяем что в URL новой вкладки содержится "dzen.ru"
