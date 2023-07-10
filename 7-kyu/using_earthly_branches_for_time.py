# https://www.codewars.com/kata/63b3cebaeb152e12268bdc02

branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
branches = branches + branches

def what_branch(time):
    h, m = map(int,time.split(':'))
    return  {i: b for i, b in enumerate(branches, -1)}[(h + 23) // 2 - 12]
