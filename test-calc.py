import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2, 2), 4)
        self.assertEqual(calc.add(-2, 2), 0)
        self.assertEqual(calc.add(-2, -2), -4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 2), 0)
        self.assertEqual(calc.subtract(-2, 2), -4)
        self.assertEqual(calc.subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 2), 4)
        self.assertEqual(calc.multiply(-2, 2), -4)
        self.assertEqual(calc.multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(calc.divide(2, 2), 1)
        self.assertEqual(calc.divide(-2, 2), -1)
        self.assertEqual(calc.divide(-2, -2), 1)


if __name__ == '__main__':
    unittest.main()
