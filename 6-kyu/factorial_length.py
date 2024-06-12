# https://www.codewars.com/kata/59f34ec5a01431ab7600005a

import math
def count(n):
    return math.ceil(math.log10(2 * math.pi * n) / 2 + n * math.log10(n / math.e))


# ceil(lgamma(n+1) / log(10))
# ceil( sum(log10(x) for x in range(1,n+1) ))
