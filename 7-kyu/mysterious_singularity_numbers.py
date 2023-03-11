# https://www.codewars.com/kata/6409aa6df4a0b773ce29cc3d

def real_numbers(n):
    div30, rem30  = divmod(n, 30)  #  30 == 2 * 3 * 5 
    part1 = div30 * sum( [ i % 2 != 0 and i % 3 != 0  and i % 5 != 0  for i in range(0,30)] )
    part2 = sum( [ i % 2 != 0 and i % 3 != 0  and i % 5 != 0  for i in range(0,rem30+1 )] )
    return part1 + part2
