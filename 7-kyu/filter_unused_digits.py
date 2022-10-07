# https://www.codewars.com/kata/55de6173a8fbe814ee000061

def unused_digits(*numbers):
    used = []
    [[used.append(i) for i in str(n)] for n in numbers]
    return ''.join(sorted({str(i) for i in range(10)}.difference(used)))
    

