# https://www.codewars.com/kata/58882bdb5edef0343400002a

def ada_number(line):
    if line.count('#') == 2 and line[-1] == '#':
        base, num, _ = line.split('#')
        if base.isnumeric() and not( 2<= int(base) <= 16):
            return False
        num = num.replace('_','')
    if line.count('#') == 0:
        base = 10
        num = line
    try:
        print(num, base)
        int(num, int(base))
        return True
    except:
        return False
