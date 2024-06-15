# https://www.codewars.com/kata/5886d65e427c27afeb0000c1

def square_digits_sequence(n):
    res = [n]
    while True:
        n = sum(int(d)**2 for d in str(n))
        if n not in res:
            res.append(n)
        else:
            res.append(n)
            break
    return len(res)

