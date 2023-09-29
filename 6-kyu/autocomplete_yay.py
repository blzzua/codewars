# https://www.codewars.com/kata/5389864ec72ce03383000484

def autocomplete(input_, dictionary):
    input_ = ''.join(c for c in input_ if c.isalpha())
    res = []
    for i in dictionary:
        if i.lower().startswith(input_):
            res.append(i)
        if len(res) == 5:
            break
    return res
