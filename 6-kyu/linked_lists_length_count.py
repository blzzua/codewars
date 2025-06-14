# https://www.codewars.com/kata/55beec7dd347078289000021

from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

def length(node: Node) -> int:
    cnt = 0
    while not(node is None):
        cnt = cnt + 1
        node = node.next
    return cnt

def count(node: Node, data) -> int:
    cnt = 0
    while not(node is None):
        if node.data == data: 
            cnt = cnt + 1
        node = node.next
    return cnt

