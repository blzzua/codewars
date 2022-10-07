# https://www.codewars.com/kata/581e476d5f59408553000a4b

def length(head): 
    cnt = 0
    while head != None:
        cnt = cnt + 1
        head = head.next
    return cnt


