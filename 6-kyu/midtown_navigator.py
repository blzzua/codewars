# https://www.codewars.com/kata/59665001dc23af735700092b

import re 
def midtown_nav(start, end):
    start_ave, start_str = [int(num) for num in re.findall('\d+', start)]
    end_ave, end_str = [int(num) for num in re.findall('\d+', end)]
    s1 = f'Walk {abs(start_str - end_str)} blocks ' + { (start_str >= end_str):'south', (start_str <= end_str): 'north'}[True]
    s2 = f', and {abs(start_ave - end_ave)} blocks ' + { (start_ave >= end_ave):'east', (start_ave <= end_ave): 'west'}[True]
    return s1 + s2

