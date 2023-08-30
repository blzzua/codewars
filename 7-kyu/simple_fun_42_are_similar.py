# https://www.codewars.com/kata/588820169ab1e053240000e0

def are_similar(a, b):
    diffs = [i for i in range(len(a)) if a[i] != b[i]]
    if diffs == []:
        return True
    elif len(diffs) != 2:
        return False
    else:
        return a[diffs[0]] == b[diffs[1]] and a[diffs[1]] == b[diffs[0]] 
