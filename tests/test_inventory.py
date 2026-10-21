import pytest
#from selenium.webdriver.common.by import By

class TestSorting:

    @pytest.mark.parametrize("sort_value, is_reverse, by_price", [
        ("az",   False, False),
        ("za",   True,  False),
        ("lohi", False, True),
        ("hilo", True,  True),
    ])
    def test_sorting(self, logged_in_page, sort_value, is_reverse, by_price):
        # Берем данные до сортировки
        if by_price:
            before = logged_in_page.get_product_prices()
        else:
            before = logged_in_page.get_product_names()

        # Применяем сортировку
        logged_in_page.choose_sorting_type(sort_value)

        # Берем данные после сортировки
        if by_price:
            after = logged_in_page.get_product_prices()
        else:
            after = logged_in_page.get_product_names()

        # Сравниваем с ожидаемым порядком
        expected = sorted(before, reverse=is_reverse)
        assert after == expected, \
            f"Сортировка '{sort_value}' не работает."
            

    
    @pytest.mark.parametrize("first, second", [
    (("az",   False, False), ("lohi", False, True)),
    (("hilo", True,  True),  ("za",   True,  False)),
])
    def test_sorting_sequence(self, logged_in_page, first, second):
        first_sort, _, _ = first
        second_sort, second_is_reverse, second_by_price = second

        base_name_sort = logged_in_page.get_product_names()
        base_price_sort = logged_in_page.get_product_prices()

        # Применяем первую сортировку
        logged_in_page.choose_sorting_type(first_sort)

        # Применяем вторую сортировку
        logged_in_page.choose_sorting_type(second_sort)

        if second_by_price:
            second_sort_res = logged_in_page.get_product_prices()
        else:
            second_sort_res = logged_in_page.get_product_names()    

        # Проверям, что вторая сортировка сработала корректно
        if second_by_price:
            expected = sorted(base_price_sort, reverse=second_is_reverse)
        else:  
            expected = sorted(base_name_sort, reverse=second_is_reverse)
        assert second_sort_res == expected, f"Вторая сортировка '{second_sort}' не работает."
