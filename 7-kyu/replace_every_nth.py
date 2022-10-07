# https://www.codewars.com/kata/57fcaed83206fb15fd00027a

def replace_nth(text, n, old, new):
    cnt = 0
    text_l = list(text)
    for i,c in enumerate(text_l):
        if c == old:
            cnt+=1
            if cnt == n:
                text_l[i] = new
                cnt = 0
    return "".join(text_l)

