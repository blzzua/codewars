# https://www.codewars.com/kata/5886cab0a95e17e61600009d

def number_of_clans(divisors, k):
    res = set()
    for i in range(1, k+1):
        clan = tuple(div for div in divisors if i % div == 0)
        res.add(clan)
    return len(res)

