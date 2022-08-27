

# The linked list is defined as follows:
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

#https://www.codewars.com/kata/581e476d5f59408553000a4b
# Fun with lists: length
def length(node):
    cnt = 0
    while node not is None:
        cnt = cnt + 1
        node = node.next
    return cnt

  

# https://www.codewars.com/kata/581c867a33b9fe732e000076
# Fun with lists: lastIndexOf
def last_index_of(node, search_val):
    last_ind = -1
    ind = 0
    while True:
        if node is None:
            break
        if node.data == search_val:
            last_ind = ind
        ind += 1
        node = node.next
    return last_ind

# https://www.codewars.com/kata/581c6b075cfa83852700021f
# translation not implemented in python. but solution is
def index_of(node, search_val):
    last_ind = -1
    ind = 0
    while True:
        if node is None:
            break
        if node.data == search_val:
            return ind
        ind += 1
    # not found
    return -1

# Fun with lists: countIf
# https://www.codewars.com/kata/5819081d056d4bdd410004f8  
def count_if(node, func):
    cnt = 0
    while True:
        if node is None:
            break
        if func(node.data):
            cnt += 1
        node = node.next
    return cnt

# Fun with lists: filter
# https://www.codewars.com/kata/582041237df353e01d000084
# translation not implemented in python. but solution is
def filter(head, pred):
    res_chain = None
    while True:
        if node is None:
            break
        if pred(node.data):
            res_chain = Node(node, res_chain)
        node = node.next
    return res_chain
  
# Fun with lists: anyMatch + allMatch
# https://www.codewars.com/kata/581e50555f59405743001813
def any_match(node, pred):
    while True:
        if node is None:
            break
        if pred(node.data):
            return True
        node = node.next
    return False

def all_match(node, pred):
    while True:
        if node is None:
            break
        if not pred(node.data):
            return False
        node = node.next
    return True
