import unittest
from unittest.mock import patch
from bread_program import calculate_bread_cost, main

class TestBreadProgram(unittest.TestCase):
    def test_calculate_bread_cost(self):
        # Тест с количеством буханок 
        bread_amount = 5
        regular_price, discounted_price, total_cost = calculate_bread_cost(bread_amount)
        self.assertEqual(regular_price, 49.0)
        self.assertEqual(discounted_price, 19.6)
        self.assertEqual(total_cost, bread_amount * discounted_price)

        # Тест с количеством буханок 0
        regular_price, discounted_price, total_cost = calculate_bread_cost(0)
        self.assertEqual(regular_price, 49.0)
        self.assertEqual(discounted_price, 19.6)
        self.assertEqual(total_cost, 0)

    @patch('builtins.input', side_effect=['f{bread_amount}'])
    def test_main_function(self, mock_input):
        # Тестирование основной функции с вводом пользователя (используется mock)
        with patch('builtins.print') as mock_print:
            main()
            

    @patch('builtins.input', side_effect=['invalid_input', 'f{bread_amount}'])
    def test_main_function_with_invalid_input(self, mock_input):
        # Тестирование основной функции с некорректным вводом пользователя
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Ошибка ввода. Пожалуйста, введите целое число для количества буханок.")

if __name__ == '__main__':
    unittest.main()
