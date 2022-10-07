# https://www.codewars.com/kata/60edafd71dad1800563cf933

def counter():
    cnt = 0
    def increment():
        nonlocal cnt
        cnt += 1
        return cnt
    return increment


