# https://www.codewars.com/kata/550554fd08b86f84fe000a58

def in_array(array1, array2):
    res = set()
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                res.add(word1)
                break
    return sorted(res)
