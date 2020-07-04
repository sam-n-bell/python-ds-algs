import unittest
from memoization import fib

class MemoizationTests(unittest.TestCase):

    def test_zero_to_two_fibs(self):
        self.assertTrue(fib(0) == 0)
        self.assertTrue(fib(1) == 1)
        self.assertTrue(fib(2) == 1)

    def test_tenth_fib(self):
        self.assertEqual(fib(10), 55)
    
    def test_one_hundreth_fib(self):
        self.assertEqual(fib(100), 354224848179261915075)

if __name__ == '__main__':
    unittest.main()