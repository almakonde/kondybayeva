import unittest
from unittest.mock import patch
from bread_program import calculate_bread_cost, main
import random

class DynamicTestMeta(type):
    def __new__(cls, name, bases, dct):
        for i in range(30):
            def test_method(self, quantity=random.randint(1, 100)):
                with self.subTest(quantity=quantity):
                    regular_price, discounted_price, total_cost = calculate_bread_cost(quantity)
                    expected_total_cost = quantity * discounted_price
                    self.assertAlmostEqual(regular_price, 49.0, places=2)
                    self.assertAlmostEqual(discounted_price, 19.6, places=2)
                    self.assertAlmostEqual(total_cost, expected_total_cost, places=2)

            test_name = f'test_{i + 1}'
            dct[test_name] = test_method

        return super().__new__(cls, name, bases, dct)

class TestBreadProgram(unittest.TestCase, metaclass=DynamicTestMeta):
    pass



if __name__ == '__main__':
    unittest.main()
