import unittest


class TestCode(unittest.TestCase):
    def test_lambda_function(self):
        add = lambda x, y: x + y
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)

    def test_list_comprehension(self):
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = [x**2 for x in numbers]
        self.assertEqual(squared_numbers, [1, 4, 9, 16, 25])

    def test_closure(self):
        def outer_function(x):
            def inner_function(y):
                return x + y
            return inner_function

        closure = outer_function(10)
        self.assertEqual(closure(5), 15)
        self.assertEqual(closure(8), 18)

    def test_higher_order_function(self):
        def apply_operation(operation, x, y):
            return operation(x, y)
        add = lambda x, y: x + y
        self.assertEqual(apply_operation(add, 5, 3), 8)
        self.assertEqual(apply_operation(add, 10, 2), 12)


if _name_ == '_main_':
    unittest.main()
