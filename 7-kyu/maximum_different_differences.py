# https://www.codewars.com/kata/63adf4596ef0071b42544b9a

import gmpy2

def max_df(a_n: int) -> int:
    # print(a_n)
    # (int((1257439209*2)**0.5)*2-1)//2
    return (gmpy2.isqrt(8 * a_n)-1)//2
