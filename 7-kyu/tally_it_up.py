# https://www.codewars.com/kata/5630d1747935943168000013

def score_to_tally(score):
    sep = ' <br>'
    e, rest = divmod(score-1, 5)
    return sep.join(['e'] * e + ['abcde'[rest]]) + (sep if rest == 4 else '')
