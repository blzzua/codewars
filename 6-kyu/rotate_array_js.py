# https://www.codewars.com/kata/54f8b0c7a58bce9db6000dc4

from numpy import roll
def rotate(arr, n):
    return roll(arr, n).tolist()
