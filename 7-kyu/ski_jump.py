# https://www.codewars.com/kata/57ed7214f670e99f7a000c73

def ski_jump(mountain):
    h = len(mountain)
    jump = round(h**2*1.5*9/10,2)
    if jump < 10:
        res = 'He\'s crap!'
    elif jump < 25:
        res = 'He\'s ok!'
    elif jump < 50:
        res = 'He\'s flying!'
    else:
        res = 'Gold!!'
    return f'{jump:.2f} metres: {res}'

