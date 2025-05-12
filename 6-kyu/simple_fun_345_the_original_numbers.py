# https://www.codewars.com/kata/59bf6c18afcda2c45100008a

def original_numbers(final_numbers,turns):
    if turns == 0:
        return final_numbers
    ssum = sum(final_numbers) // (len(final_numbers)-1)
    prev_numbers = [ssum - num for num in final_numbers]
    return original_numbers(prev_numbers,turns - 1)

