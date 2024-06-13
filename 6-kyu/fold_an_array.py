# https://www.codewars.com/kata/57ea70aa5500adfe8a000110

def fold_array(array, runs):
    if runs == 0:
        return array
    res = array[:]
    mid  = len(array) // 2
    for i in range(mid):
        res[i] += res.pop()
    return fold_array(res, runs-1)
