# https://www.codewars.com/kata/5d9fe0ace0aad7001290acb7

def number_of_sigfigs(number):
    if '.' in number:
        return len(number.lstrip('0')) - 1 
    else:
        return len(number.strip('0'))
