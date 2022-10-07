# https://www.codewars.com/kata/5a512f6a80eba857280000fc

from heapq import nsmallest
def nth_smallest(arr, pos):
    return nsmallest(pos,arr)[-1]

