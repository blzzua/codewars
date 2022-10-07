# https://www.codewars.com/kata/57fafb6d2b5314c839000195

def remove(s):
    return ' '.join(w for w in s.split(' ') if not(w.count('!') == 1))

