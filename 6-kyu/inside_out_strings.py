# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5

def roll(word):
    l = len(word)
    if l <= 3:
        return word
    word = list(word)
    m = l//2
    res = word[:m][::-1] + ([word[m]] if l % 2 else []) + word[-m:][::-1]
    return ''.join(res)
    
def inside_out(st):
    return ' '.join(map(roll,st.split(' ')))
