# https://www.codewars.com/kata/5d7c7697e8ad48001e642964

def cube_times(times):
    times.sort()
    return round(sum(times[1:-1])/3,2), times[0]

