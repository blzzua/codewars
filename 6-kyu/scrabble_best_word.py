# https://www.codewars.com/kata/563f960e3c73813942000015

from string import ascii_uppercase as al

def get_best_word(points, words):
    def scores(word):
        return sum(points[al.index(ch)] for ch in word)
    best_word_index, best_word_score = 0, 0
    for i, word in enumerate(words):
        cur_word_score = scores(word)
        if best_word_score < cur_word_score or (best_word_score == cur_word_score and len(words[best_word_index]) > len(word)):
            best_word_index = i
            best_word_score = cur_word_score
    return best_word_index
