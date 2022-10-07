# https://www.codewars.com/kata/5df261342964c80028345a0a

def check_parity(parity, bin_str): 
    return (parity == 'odd') ^ (bin_str.count('1') & 1)

