# https://www.codewars.com/kata/57029e77005264a3b9000eb5

def nothing_special(s):
    if isinstance(s,str):
        return ''.join(c for c in s if (c.isalnum() or c in ' \t'))
    else:
        return 'Not a string!'

# re: [^a-z0-9\s]
