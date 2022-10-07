# https://www.codewars.com/kata/592a33e549fe9840a8000ba1

def is_even(n):
    return (n - 10 * (n // 10)) in (0, 2, 4, 6, 8)

