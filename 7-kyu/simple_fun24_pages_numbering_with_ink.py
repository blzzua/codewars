# https://www.codewars.com/kata/5886da134703f125a6000033

def pages_numbering_with_ink(current, number_of_digits):
    while number_of_digits:
        cur_len = len(str(current))
        if number_of_digits >= cur_len:
            number_of_digits -= cur_len
            current = current+1
        else:
            break
    return current - 1

