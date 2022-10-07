# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

def reverse_words(text):
  return ' '.join([w[::-1] for w in text.split(' ')])

