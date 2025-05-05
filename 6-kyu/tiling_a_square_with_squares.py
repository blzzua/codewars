# https://www.codewars.com/kata/62fd308673fd4b9397117c91
def num_tiles(n):
    bins = []
    while n:
        n, bit = divmod(n,2)
        bins.append(bit * 2 ** len(bins))
    prev_square_len = 0
    res = 0
    for cur_square_len in bins[::-1]:
        if cur_square_len != 0:
            res += ((prev_square_len + cur_square_len) ** 2 - (prev_square_len) ** 2) // (cur_square_len**2)
            prev_square_len += cur_square_len
    return res


# clever:
res = 0
while n:
    n, bit = divmod(n,2)
    res += bit * ((4*n)+1) # multiply on bit instead sum if bit == 1: 
return res

