# https://www.codewars.com/kata/587a88a208236efe8500008b

def sequence_sum(begin_number, end_number, step):
    if step * (end_number - begin_number) < 0:
        return 0
    coeff = (end_number - begin_number) // step
    return  begin_number + coeff * begin_number + int(coeff * step * coeff   + step * coeff  )//2
