# https://www.codewars.com/kata/581c6b075cfa83852700021f

def index_of(head, value): 
    find_ind = -1
    ind = 0
    node = head
    while True:
        if node is None:
            break
        if node.data == value:
            find_ind = ind
            break
        ind += 1
        node = node.next
    return find_ind

