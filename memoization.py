import unittest
sequences = dict()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if sequences.get(n - 2) is None:
            sequences[n - 2] = fib(n - 2)
        if sequences.get(n - 1) is None:
            sequences[n - 1] = fib(n - 1)
        return sequences.get(n - 2) + sequences.get(n - 1)

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

