# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people):
    res = []
    for i, char in enumerate(people):
        if char == ' ':
            continue
        nl = list(people)
        nl[i] = char.upper()
        res.append(''.join(nl))
    return res

