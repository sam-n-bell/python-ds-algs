import unittest

def is_palindrome(string: str) -> bool:
    if len(string) < 2:
        return False
        
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            # left and right characters don't match
            return False
        left += 1
        right -= 1

    # got all the way through
    return True

class PalindromeTests(unittest.TestCase):

    def test_even_count_palindrome(self):
        self.assertTrue(is_palindrome('hannah'))

    def test_odd_count_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('alex'))
    
    def test_not_palindrome_single_char(self):
        self.assertFalse(is_palindrome('b'))
    
    def test_not_palindrome_empty_string(self):
        self.assertFalse(is_palindrome(''))
        
if __name__ == '__main__':
    unittest.main()