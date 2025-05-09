# https://www.codewars.com/kata/57d307fb9d84633c5100007a

def range_parser(s):
    parts = []
    res = []
    for part in s.split(', '):
        if ',' in part:
            parts.extend(part.split(','))
        else:
            parts.append(part)
    for part in parts:
        if ':' in part:
            part, _, step = part.partition(':')
            step = int(step)
        else:
            step = 1
        if '-' in part:
            start, _, finish = part.partition('-')
            start, finish = int(start), int(finish)
            res.extend(list(range(start, finish+1, step)))
        else:
            res.append(int(part))
    return res


