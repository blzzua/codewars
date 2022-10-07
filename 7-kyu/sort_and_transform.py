# https://www.codewars.com/kata/57cc847e58a06b1492000264

def sort_transform(arr, batch=4):
    #return '-'.join(''.join(map(chr,chars)) for chars in zip(*(arr[diff:] for diff in range(batch))))
    def ch(s):return ''.join(map(chr,s[:2]+s[-2:]))
    return '-'.join([ch(arr), ch(sorted(arr)), ch(sorted(arr, reverse=True)), ch(sorted(arr))])

