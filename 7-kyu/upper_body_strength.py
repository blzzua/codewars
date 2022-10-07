# https://www.codewars.com/kata/571640812ad763313600132b

def alex_mistakes(number_of_katas, time_limit):
    time_limit -= 60 * number_of_katas // 10
    i = 0
    while True:
        time_limit = time_limit - 5 * 2**i
        if time_limit < 0:
            break
        else:
            i = i + 1
    return i

