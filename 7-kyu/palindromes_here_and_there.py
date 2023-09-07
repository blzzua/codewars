# https://www.codewars.com/kata/5838a66eaed8c259df000003

def convert_palindromes(numbers):
    return [*map(int,map(lambda s: s == s[::-1] ,map(str,numbers)))]
