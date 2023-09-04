# https://www.codewars.com/kata/5705601c5eef1fad69000674

def to_bytes(n):
    res = []
    while n:
        n,d = divmod(n, 256)
        res.append(bin(d)[2:].zfill(8))
    return res[::-1] or ['00000000']
  
