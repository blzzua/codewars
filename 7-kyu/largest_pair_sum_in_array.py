# https://www.codewars.com/kata/556196a6091a7e7f58000018

def largest_pair_sum(numbers): 
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]

