# https://www.codewars.com/kata/52f3bb2095d6bfeac2002196

def valid_word(seq, word):
    if len(word) > 0:
        for part in seq:
            if word.startswith(part):
                rest = word[len(part):]
                if valid_word(seq, rest):
                    return True
        return False
    else:
        return True
