# https://www.codewars.com/kata/57af26297f75b57d1f000225

def truncate_string(s, n):
    if len(s) <= n:
        return s
    else:
        if n <= 3:
            return s[:n] + '...'
        else:
            return s[:n-3] + '...'
