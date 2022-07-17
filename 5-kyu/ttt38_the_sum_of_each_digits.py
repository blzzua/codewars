# https://www.codewars.com/kata/57b1f617b69bfc08cf00042a

# naive solution, works. but perfomance issues: 
def sum_of_digits(a, b):
  return sum(int(n) for n in ''.join([str(i) for i in range(a,b+1)]))


# cheat. for spy other solutions:
def sum_of_digits(a, b):
    def f(n):
        d, m, s = 0, 1, 0
        while n:
            n, r = divmod(n, 10)
            s += r * 9 * d * 10 ** d // 2 + r * (r-1) // 2 * 10 ** d + r * m
            m += r * 10 ** d
            d += 1
        return s
    return f(b) - f(max(a-1, 0))
