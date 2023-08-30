# https://www.codewars.com/kata/5d72704499ee62001a7068c7

def oddest(a):
    # negative binary workaround
    arr_bin = [list(bin( ((1<<32)+i) if i<0 else i)[2:][::-1]) for i in a]
    index = max(range(len(arr_bin)), key=lambda i: arr_bin[i])
    return a[index]
