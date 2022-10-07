# https://www.codewars.com/kata/558fa34727c2d274c10000ae

def scrabble_score(st): 
    return sum(dict_scores[c] for c in st.upper().replace(' ', ''))

