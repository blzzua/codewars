# https://www.codewars.com/kata/586efc2dcf7be0f217000619

def reverse_slice(s):
    return [s[:i+1][::-1] for i in range(len(s))][::-1]
