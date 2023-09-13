# https://www.codewars.com/kata/59824f384df1741e05000913

def most_common(s):
    return ''.join(sorted(s, key=lambda c:s.count(c), reverse=True))
