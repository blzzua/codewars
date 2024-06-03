# https://www.codewars.com/kata/59f2746e50c8c2b55d000085

def conv(num):
    len_odd = bool(len(str(num)) % 2)
    res = []
    for i, digit in enumerate(str(num),1):
        if int(digit) % 2 == len_odd:
            dig_name = 'zero one two three four five six seven eight nine'.split()[int(digit)]
            dig_line=''
            for j in range(i):
                 dig_line = dig_line + (dig_name.lower() if j % 2 == len_odd else dig_name.upper())
            res.append(dig_line[:i])
        else:
            res.append(digit)
    return ''.join(res)
