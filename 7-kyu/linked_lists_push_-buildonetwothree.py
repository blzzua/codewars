# https://www.codewars.com/kata/55be95786abade3c71000079

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new = Node(data)
    if head is None:
        return new
    else:
        new.next = head
    return new

def build_one_two_three():
    return push(push(Node(3), 2), 1)
