# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0

def solution(n,d):
    if d <= 0:
        return []
    else:
        return [int(num) for num in str(n)[-d:]]

