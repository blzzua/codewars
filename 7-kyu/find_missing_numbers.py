# https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb

def find_missing_numbers(arr):
    if len(arr)>1:
        return [i for i in  range(min(arr),-~max(arr)) if i not in arr]
    else:
        return []

