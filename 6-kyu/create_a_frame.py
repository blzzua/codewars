# https://www.codewars.com/kata/5672f4e3404d0609ec00000a

def frame(text, char):
    width = max((len(line) for line in text))
    res = [(width + 4) * char]
    for row in text:
        res.append(char + ' ' + row + ' ' * (width - len(row)) + ' ' + char )
    res.append((width + 4) * char)
    return '\n'.join(res)
