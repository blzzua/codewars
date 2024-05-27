# https://www.codewars.com/kata/63efd90145e04e000f697d85

def the_intervals(intervals,numbers):
    res = []
    for number in numbers:
        accepted_intevals = []
        for a, b in intervals:
            if a < number < b:
                accepted_intevals.append(f'({a};{b})')
        if accepted_intevals:
            res.append(f'{number} ∈ ' + ' ∩ '.join(accepted_intevals) )
    return ' and '.join(res)
