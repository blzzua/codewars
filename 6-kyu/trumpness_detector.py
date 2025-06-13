# https://www.codewars.com/kata/57829376a1b8d576640000d6

import re
def trump_detector(trump_speech):
    vowels = re.findall(r'[aA]+|[eE]+|[iI]+|[oO]+|[uU]+', trump_speech)
    if not vowels:
        return 0
    add_vowel = 0
    for v_seq in vowels:
        if len(v_seq) > 1:
            add_vowel += len(v_seq) - 1
    return round(add_vowel / len(vowels), 2)
