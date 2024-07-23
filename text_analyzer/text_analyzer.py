import re

def count_words(text):
  """Counts the number of words in a given text."""
  words = re.findall(r'\w+', text)
  return len(words)

def count_sentences(text):
  """Counts the number of sentences in a given text."""
  sentences = re.split(r'[.!?]', text)
  return len(sentences) - 1

def count_average_word_length(text):
  """Calculates the average word length in a given text."""
  words = re.findall(r'\w+', text)
  total_length = sum(len(word) for word in words)
  return total_length / len(words) if words else 0

def most_common_word(text):
  """Finds the most common word in a given text."""
  words = re.findall(r'\w+', text.lower())
  word_counts = {}
  for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
  return max(word_counts, key=word_counts.get)

