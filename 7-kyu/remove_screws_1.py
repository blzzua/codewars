# https://www.codewars.com/kata/57109bf197b4b3853a000274

def sc(s):
    cur_scd = s[0]
    time = 0
    for sc in s:
        if cur_scd != sc:
            cur_scd = sc
            time += 6
        else:
            time +=1
    return time + len(s)-1 
    
# golf version
sc=lambda s:2*len(s)-1+5*(s.count('+-')+s.count('-+'))
