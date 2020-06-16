import unittest
import anagram

class TestAnagram(unittest.TestCase):

    # test_ required in method name
    def test_anagram_happy_path(self):
        self.assertTrue(anagram.are_anagrams('race', 'care'))

    def test_anagram_ignore_case(self):
        self.assertTrue(anagram.are_anagrams('race', 'CARE'))

    def test_anagram_negative_path(self):
        self.assertFalse(anagram.are_anagrams('sam', 'josh'))

    def test_anagram_none_variable(self):
        self.assertFalse(anagram.are_anagrams(None, 'Joel'))

    def test_anagram_empty_string_variable(self):
        self.assertFalse(anagram.are_anagrams('', 'Sam'))

