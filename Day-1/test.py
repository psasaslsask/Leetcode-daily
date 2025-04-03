import unittest
from main import mergeAlternately  # This must match the filename: 'main.py'

class TestMergeAlternately(unittest.TestCase):

    def test_equal_length(self):
        self.assertEqual(mergeAlternately("abc", "123"), "a1b2c3")

    def test_word1_longer(self):
        self.assertEqual(mergeAlternately("abcd", "12"), "a1b2cd")

    def test_word2_longer(self):
        self.assertEqual(mergeAlternately("ab", "1234"), "a1b234")

    def test_empty_word1(self):
        self.assertEqual(mergeAlternately("", "xyz"), "xyz")

    def test_empty_word2(self):
        self.assertEqual(mergeAlternately("xyz", ""), "xyz")

    def test_both_empty(self):
        self.assertEqual(mergeAlternately("", ""), "")

if __name__ == '__main__':
    unittest.main()
