# https://www.codewars.com/kata/5f55ecd770692e001484af7d

def mirror(data: list) -> list:
    return sorted(data) + sorted(data,reverse=True)[1:]


