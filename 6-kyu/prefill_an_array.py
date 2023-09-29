# https://www.codewars.com/kata/54129112fb7c188740000162

def prefill(n,v = None):
    try:
        n = int(n)
        return [v] * n
    except (ValueError, TypeError) as e:
        return 'xyz is invalid'
