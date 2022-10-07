# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a

def sort_vowels(s):
    if isinstance(s, str):
        res = []
        for i in s:
            if i.lower() in 'aeiou':
                res.append('|'+ i)
            else:
                res.append(i + '|')
        return '\n'.join(res)
    else:
        return ''
    

