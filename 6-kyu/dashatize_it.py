# https://www.codewars.com/kata/58223370aef9fc03fd000071

def dashatize(n):
    res = []
    for d in str(n):
        if d in '13579':
            res.append(d)
        else:
            if res and res[-1][-1] in '02468':
                add = res.pop() + d
            else:
                add = d
            res.append(add)
    return '-'.join(res).lstrip('-')
  
