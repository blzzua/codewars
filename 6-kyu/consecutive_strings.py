# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    if k <= 0:
        return ''
    longest = ''
    for i in range(len(strarr) - k + 1):
        test = ''.join(strarr[i:i+k])
        if len(longest) < len(test):
            longest = test
    return longest

