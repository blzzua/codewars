# https://www.codewars.com/kata/581c867a33b9fe732e000076

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

