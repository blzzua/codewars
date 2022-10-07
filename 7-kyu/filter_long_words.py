# https://www.codewars.com/kata/5697fb83f41965761f000052

def filter_long_words(sentence, n):
    return [*filter(lambda w: len(w)>n, sentence.split())]


