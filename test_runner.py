import unittest
import math_utils   # the file we are testing ,from  math_utils.py

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_utils.add(2, 3), 5)
        self.assertEqual(math_utils.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(math_utils.multiply(2, 3), 6)
        self.assertEqual(math_utils.multiply(-1, 5), -5)

if __name__ == "__main__":
    unittest.main()
