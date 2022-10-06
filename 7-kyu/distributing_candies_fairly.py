# https://www.codewars.com/kata/59901cd68fc658ab6c000025

def distribute(m, n):
    m = max(0,m)
    if n <= 0:
        return []
    eq, rest = divmod(m,n)
    return [eq +1 if i < rest else eq for i in range(n)  ]

