# https://www.codewars.com/kata/585eaef9851516fcae00004d

def what_list_am_i_on(actions):
    res = sum(1 if w[0] in 'gsn' else -1 if w[0] in 'bdk' else 0 for w in actions)
    if res > 0:
        return 'nice'
    else:
        return 'naughty'
