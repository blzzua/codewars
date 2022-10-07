# https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2

from itertools import starmap
def solve(arr):
    def conv(t1,t2):
        t1 = tuple(map(int,t1.split(":")))
        t2 = tuple(map(int,t2.split(":")))
        hd1, md = divmod((t2[1] - t1[1] - 1), 60)
        hd2 = (t2[0] - t1[0] + hd1) % 24 
        mm = (hd2 % 24) * 60 + md
        return mm, ':'.join(str(c).zfill(2) for c in divmod(mm, 60))
    arr = sorted(set(arr))
    return max(starmap(conv,zip(arr,arr[1:]+arr)))[1]
