# https://www.codewars.com/kata/5959b637030042889500001d

from collections import Counter 
import numpy as np

def prepare_all():
    num2letters_map =  {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'}
    n2l_cntr = {}
    for k in num2letters_map:
        n2l_cntr[str(k)] = Counter(num2letters_map[k])
    all_letters = list(set(list(''.join(i for i in num2letters_map.values()))))
    all_numbers = ''.join(num2letters_map.keys())
    A = np.zeros((len(all_letters), len(all_numbers)), dtype=int)
    for j,letter in enumerate(all_letters):
        for i, number in enumerate(all_numbers):
            A[j][i] = n2l_cntr[number].get(letter,0)
    return A, all_letters, all_numbers

A, all_letters,all_numbers =  prepare_all()

def original_number(s):
    cntr = Counter(s)
    B = np.array([cntr[c] for c in all_letters])
    res = np.linalg.lstsq(A, B)
    return ''.join([letter * count for letter, count in zip(all_numbers, res[0].round().astype(int))])

