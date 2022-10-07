# https://www.codewars.com/kata/5710a50d336aed828100055a

def sc(s):
    print(s)
    cur_scd = s[0]
    time = 0
    for sc in s:
        if cur_scd != sc:
            cur_scd = sc
            time += 6
        else:
            time +=1
    return time + len(s)-1 
            
            

