# https://www.codewars.com/kata/579ba41ce298a73aaa000255

def name_that_number(x):
    names =  {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if x in names:
        return names.get(x)
    tens, ones = divmod(x, 10)
    res = [names.get(tens*10)]
    if ones > 0:
        res.append(names.get(ones))
    return ' '.join(res)
