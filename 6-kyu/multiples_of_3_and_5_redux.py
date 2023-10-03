# https://www.codewars.com/kata/54bb6ee72c4715684d0008f9

def solution(number):
    # return sum(filter(lambda x: (x % 3 ) * (x % 5) == 0, range(number)))
    n = number - 1
    s3, s5, s15 = [i*(n // i)*((n // i) + 1) // 2 for i in (3, 5, 15)]
    return s3 + s5 - s15
