# https://www.codewars.com/kata/5a91a7c5fd8c061367000002

def minimum_steps(numbers, value):
    step = 0
    for i, n in enumerate(sorted(numbers)):
        step += n
        if step >= value: 
            return i
        

