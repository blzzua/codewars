# https://www.codewars.com/kata/65013fc50038a68939098dcf

def party_people(lst):
    for i,c in list(enumerate(sorted(lst),1))[::-1]:
        if i >= c:
            return i
    return 0
