import unittest

def add(a, b):
    return a + b


class TestAddition(unittest.TestCase):  # We are inheriting code from the TestCase class!
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

# Start Main Body
unittest.main()
