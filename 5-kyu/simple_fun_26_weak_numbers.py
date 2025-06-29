# https://www.codewars.com/kata/5886dea04703f1712d000051

from functools import lru_cache

@lru_cache(1000)
def divcnt(n):
    return sum(n % (i + 1) == 0 for i in range(n))


@lru_cache(1000)
def weakcnt(n):
    return sum([divcnt(j) > divcnt(n) for j in range(n)])

def weak_numbers(n):
    max_weak = max(weakcnt(i) for i in range(1, n+1))
    same_weak = sum(weakcnt(i) == max_weak for i in range(1,n+1))
    return [max_weak, same_weak]

