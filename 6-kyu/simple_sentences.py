# https://www.codewars.com/kata/5297bf69649be865e6000922

def make_sentences(parts):
    res = []
    for part in parts:
        if res == []:
            res.append(part)
            continue
        if part == ',':
            res.append(part)
            res.append(' ')
        elif part == '.':
            if res[-1] != '.':
                res.append(part)
        else: #words
            if res[-1] != ' ':
                res.append(' ')
                res.append(part)
            else:
                res.append(part)
    if res[-1] != '.':
        res.append('.')
    return ''.join(res)


