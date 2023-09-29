# https://www.codewars.com/kata/558c04ecda7fb8f48b000075

def same(arr_a, arr_b):
    if len(arr_a) != len(arr_b):
        return False
    for a, b in zip(arr_a, arr_b):
        a.sort()
        b.sort()
    arr_a.sort()
    arr_b.sort()
    for a, b in zip(arr_a, arr_b):
        if a != b:
            return False
    else:
        return True
    
# clever: sorted(map(sorted, arr_a)) == sorted(map(sorted, arr_b))
