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

