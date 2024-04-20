# https://www.codewars.com/kata/59128363e5bc24091a00006f

from string import ascii_lowercase as al
def the_janitor(word):
    res = []
    for x in al:
        start = word.find(x)
        end = word.rfind(x)
        res.append(end - start + 1 if start != -1 else 0)
    return res
