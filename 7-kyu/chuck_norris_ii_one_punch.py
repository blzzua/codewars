# https://www.codewars.com/kata/57057a035eef1f7e790009ef

def one_punch(item): 
    if isinstance(item, str) and item:
        return ''.join(c for c in ' '.join(sorted(item.split(' '))) if c.lower() not in ('a','e'))
    else:
        return 'Broken!'

