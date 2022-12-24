# https://www.codewars.com/kata/553a2461098c64ae53000041

# extented solution of name_that_number.py: https://www.codewars.com/kata/579ba41ce298a73aaa000255

def wordify(n):
    names =  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if n in names:
        return names.get(n)
    hundreds, rem = divmod(n, 100)
    tens, ones = divmod(rem, 10)
    res = []
    if hundreds > 0:
        res.append(names.get(hundreds))
        res.append('hundred')
    if rem in names:
        res.append(names.get(rem))
    elif tens > 0:
        res.append(names.get(tens*10))
    if ones > 0 and tens > 1:
        res.append(names.get(ones))
    print(n, " to ", res, hundreds, tens, ones)
    return ' '.join(res)
