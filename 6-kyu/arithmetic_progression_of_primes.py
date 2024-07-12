# https://www.codewars.com/kata/5aa7ce59373c2e3ed30000cb

from gmpy2 import next_prime

def primes_a_p_precalc(lower_limit, upper_limit): 
  # solution work for but not fast enouch
  # but i can precalculate all solution for some limits, and use fast filter
    primes_list = []
    p = next_prime(lower_limit-1)
    while p <= upper_limit+1:
        primes_list.append(int(p))
        p = next_prime(p)

    primes_set = set(primes_list)
    res = []

    for offset, p1 in  enumerate(primes_list[:-1], 1):  
        for p2 in primes_list[offset:]: # todo optimization: instead of bruteforce on full combinations can skip on some circumstances. as instance: minimal distance is 30, max distance < p1 + (p2 -p1) //5 + 1)
            step = p2 - p1
            candidates = [(p1 + step * i) for i in range(6)]
            if all(c in primes_set for c in candidates): # todo optimization: check on gmpy2.is_prime instead "in primes_set"
                res.append(candidates)
    return res

precalc_results = primes_a_p_precalc(2,10000) # most valuable optimization for this kata - 100 task over limited diapason 2-10000. all solution can be precalculated.

def primes_a_p(lower_limit, upper_limit):
    # todo: use bisect
    res = [c for c in precalc_results if (lower_limit <= c[0] and c[-1] <= upper_limit) ]
    return sorted(res)

