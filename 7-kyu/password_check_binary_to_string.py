# https://www.codewars.com/kata/5a731b36e19d14400f000c19

def decode_pass(pass_list, bits):
    string =  ''.join(chr(int(b, 2)) for b in bits.split(' '))
    if string in pass_list:
        return string
    else:
        return False

