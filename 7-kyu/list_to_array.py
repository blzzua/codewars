# https://www.codewars.com/kata/557dd2a061f099504a000088

def list_to_array(node):
    res = [node.value]
    while not node.next is None :
        node = node.next
        res.append(node.value)       
    return res
