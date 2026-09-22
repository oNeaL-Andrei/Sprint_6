import pytest  # Подключаем pytest
from pages.main_page import MainPage  # Импортируем класс главной страницы
from data import FaqData  # Импортируем данные ответов FAQ 

class TestFAQ:  # Класс для тестов блока "Вопросы о важном"

    @pytest.mark.parametrize("index, expected_answer", FaqData.FAQ_DATA_LIST)  # Параметризация по всем 8 вопросам
    def test_faq_answers(self, driver, index, expected_answer):  # Тест проверки текста ответа FAQ
        main_page = MainPage(driver)  # Создаем объект главной страницы
        main_page.click_faq_question(index)  # Прокручиваем к вопросу и кликаем по нему
        actual_answer = main_page.get_faq_answer_text(index)  # Получаем фактический текст ответа
        assert actual_answer == expected_answer  # Сравниваем полученный текст с ожидаемым