# https://www.codewars.com/kata/5a043724ffe75fbab000009f

def reverse_middle(lst):
    mid = len(lst) // 2
    from_ = mid - 1
    to_ = mid + 1 + len(lst) % 2
    return lst[from_:to_][::-1]
