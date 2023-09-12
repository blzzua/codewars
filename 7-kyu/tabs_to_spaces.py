# https://www.codewars.com/kata/5779474882d7d0a10f000005

def tab_to_spaces(text):
    res = []
    pad = 4
    for line in text.split('\n'):
        while '\t' in line:
            i = line.index('\t')
            replacement = ' ' * (pad - (i % pad))
            line = line.replace('\t', replacement, 1)
            print(f'found at {i} = line={line}')
        res.append(line)
    return '\n'.join(res)
