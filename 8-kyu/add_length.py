# https://www.codewars.com/kata/559d2284b5bb6799e9000047

def add_length(str_):
    return [w + ' ' + str(len(w)) for w in str_.split()]

