# https://www.codewars.com/kata/5d62961d18198b000e2f22b3

def generate_number(squad, n):
    print(squad, n)
    if n not in squad:
        return n
    for i in range(11, 100):
        if  i % 10 != 0 and sum(divmod(i,10)) == n and i not in squad:
            return i
