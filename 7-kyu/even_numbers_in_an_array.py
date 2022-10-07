# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c

def even_numbers(arr,n):
    return [i for i in arr if i%2 == 0][-n:]

