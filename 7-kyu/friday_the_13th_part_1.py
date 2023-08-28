# https://www.codewars.com/kata/5925acf31a9825d616000e74

def kill_count(counselors, jason):
    return [c[0] for c in  counselors if c[1] < jason]
