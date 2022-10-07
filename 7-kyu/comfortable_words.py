# https://www.codewars.com/kata/56684677dc75e3de2500002b

def comfortable_word(word):
    l = 'q, w, e, r, t, a, s, d, f, g, z, x, c, v, b'.split(', ')
    r = 'y, u, i, o, p, h, j, k, l, n, m'.split(', ')

    cur_hand = l if word[0] in l else r
    for c in word:
        if c in cur_hand:
            cur_hand = l if cur_hand == r else r
        else:    
            return False
    return True

