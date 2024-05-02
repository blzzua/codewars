# https://www.codewars.com/kata/543e926d38603441590021dd

from itertools import permutations
def get_words(hash_of_letters):
    all_letters = ''
    for l, letters in hash_of_letters.items():
        all_letters += ''.join(l * letter for letter in letters)
    return list(sorted(set([''.join(comb) for comb in permutations(all_letters)])))
