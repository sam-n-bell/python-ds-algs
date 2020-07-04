from collections import Counter
import unittest

def are_anagrams(string1: str, string2: str) -> bool:
    if not string1 or not string2 or len(string1) != len(string2):
        return False

    return Counter(string1.lower()) == Counter(string2.lower())

class AnagramTests(unittest.TestCase):

    def test_anagram_happy_path(self):
        self.assertTrue(are_anagrams('race', 'care'))

    def test_anagram_ignore_case(self):
        self.assertTrue(are_anagrams('race', 'CARE'))

    def test_anagram_negative_path(self):
        self.assertFalse(are_anagrams('sam', 'josh'))

    def test_anagram_none_variable(self):
        self.assertFalse(are_anagrams(None, 'Joel'))

    def test_anagram_empty_string_variable(self):
        self.assertFalse(are_anagrams('', 'Sam'))

if __name__ == '__main__':
    unittest.main()