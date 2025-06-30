# https://www.codewars.com/kata/59f08f89a5e129c543000069

def dup(arry):
    res = []
    for word in arry:
        prev = ''
        res_word = ''
        for letter in word:
            if letter != prev:
                res_word += letter
                prev = letter
            else:
                pass
        res.append(res_word)
    return res

# clever tools:
re.sub(r'(\w)\1+', r'\1', word) # re
''.join(char for char, grouper in itertools.groupby(word)) # itertools.groupby
