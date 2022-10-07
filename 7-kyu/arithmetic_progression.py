# https://www.codewars.com/kata/55caf1fd8063ddfa8e000018

def arithmetic_sequence_elements(a, d, n):
    if d:
        return ', '.join(str(i) for i in range(a, a+d*n, d))
    else:
        return ', '.join(str(i) for i in [a] * n)

