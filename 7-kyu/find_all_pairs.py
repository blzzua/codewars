# https://www.codewars.com/kata/5c55ad8c9d76d41a62b4ede3

def duplicates(arr):
    return sum(arr.count(num) // 2 for num in set(arr))

