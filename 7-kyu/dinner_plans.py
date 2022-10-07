# https://www.codewars.com/kata/57212c55b6fa235edc0002a2

def common_ground(s1,s2):
    s1 = s1.split()
    s2 = s2.split()
    ss1 = set(s1)
    ss2 = set(s2)
    common = ss1.intersection(ss2)
    if common:
        return ' '.join(sorted(common, key=s2.index))
    else:
        return 'death'

