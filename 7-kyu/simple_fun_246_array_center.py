# https://www.codewars.com/kata/590bdaa251ab8267b800005b

from statistics import mean

def array_center(arr):
    return [i for i in arr if abs(i-mean(arr)) < min(arr)]

