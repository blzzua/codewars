# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    odds = {k:v for k,v in enumerate(source_array) if v % 2 == 1}
    sorted_odds = sorted(odds.values(), reverse = True)
    for i, val in enumerate(source_array):
        if val % 2 == 1:
            source_array[i] = sorted_odds.pop()
    return source_array
