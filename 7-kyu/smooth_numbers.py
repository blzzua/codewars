# https://www.codewars.com/kata/5b2f6ad842b27ea689000082

def is_smooth(n):
    def factors(n):
        f = []
        for i in (7, 5, 3, 2):
            while n % i == 0:
                n = n / i
                f.append(i)
        if n > 0:
            return f + [n]
        return f
    variants = {2: 'power of 2', 3: '3-smooth', 5: 'Hamming number', 7: 'humble number'}
    return variants.get(max(factors(n)), 'non-smooth')





