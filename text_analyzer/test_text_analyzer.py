import unittest
from text_analyzer import count_words, count_sentences, count_average_word_length, most_common_word

class TestTextAnalyzer(unittest.TestCase):

  def test_count_words(self):
    self.assertEqual(count_words("This is a test."), 4)
    self.assertEqual(count_words(" "), 0)
    self.assertEqual(count_words("One, two, three."), 3)

  def test_count_sentences(self):
    self.assertEqual(count_sentences("This is a sentence."), 1)
    self.assertEqual(count_sentences("This is a sentence. This is another."), 2)
    self.assertEqual(count_sentences("."), 1)

  def test_count_average_word_length(self):
    self.assertEqual(count_average_word_length("hello world"), 5.0)
    self.assertEqual(count_average_word_length(" "), 0)
    self.assertEqual(count_average_word_length("one two three four"), 3.5, tol=0.25)

  def test_most_common_word(self):
    self.assertEqual(most_common_word("the quick brown fox jumps over the lazy dog"), "the")
    self.assertEqual(most_common_word("apple banana apple orange"), "apple")
    self.assertEqual(most_common_word(""), "")


if __name__ == '__main__':
  unittest.main()
