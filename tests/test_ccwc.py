import unittest
from challenge_1_wc_tool.ccwc import (count_bytes_in_text, count_words_in_text, count_lines_in_text,
                                      count_characters_in_text)

class TestCCWC(unittest.TestCase):
    def test_count_bytes_in_text(self):
        text = "This is a test"
        byte_count = count_bytes_in_text(text)
        self.assertEqual(byte_count, 14)  # Replace with the expected result

    def test_count_words_in_text(self):
        text = "This is a test"
        word_count = count_words_in_text(text)
        self.assertEqual(word_count, 4)  # Replace with the expected result

    def test_count_lines_in_text(self):
        text = "Line 1\nLine 2\nLine 3"
        line_count = count_lines_in_text(text)
        self.assertEqual(line_count, 3)  # Replace with the expected result

    def test_count_characters_in_text(self):
        text = "你好"
        char_count = count_characters_in_text(text)
        self.assertEqual(char_count, 2)  # Replace with the expected result


if __name__ == '__main__':
    unittest.main()
