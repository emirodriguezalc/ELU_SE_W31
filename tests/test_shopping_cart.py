import unittest

from ..shopping_cart import calculate_total, display_total


class TestShoppingCartFunctions(unittest.TestCase):
    def test_calculate_total(self):
        cart_empty = []
        self.assertEqual(calculate_total(cart_empty), 0.0)

        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        self.assertEqual(calculate_total(cart), 25.47)

    def test_display_total(self):
        import io
        from unittest.mock import patch

        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]

        expected_output = "Total price: 25.47\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            display_total(calculate_total(cart))
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
