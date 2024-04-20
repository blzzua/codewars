# https://www.codewars.com/kata/56e8d06029035a0c7c001d85

from preloaded import adapt_size, display

adapt_size(0.9)     # You can adjust the size of the cells, so that your heart is displayed better
# display(heart)    # To see your (he)art


def draw(n):
    h = n //2
    res = []
    res.append( ('◢' + '■' * (h-2) + '◣' ) * 2 )
    for i in range(n//6):
        res.append( '■' * n )
    for i in range(n-2, -1, -2):
        res.append(' ' * (h-i//2-1) + '◥' + '■' * i + '◤' + ' ' * (h-i//2-1))
    return '\n'.join(res)
