# https://www.codewars.com/kata/5a0aae48ba2a14cfa600016d

def start_smoking(bars,boxes):
    return  int(sum((bars*10*18+boxes*18)/(5**i) for i in range(10)))

