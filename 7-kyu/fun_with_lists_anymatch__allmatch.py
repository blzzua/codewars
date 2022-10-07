# https://www.codewars.com/kata/581e50555f59405743001813

from typing import Callable, Any

def any_match(node: Node, pred: Callable[[Any], bool]) -> bool:
    while True:
        if node is None:
            break
        if pred(node.data):
            return True
        node = node.next
    return False

def all_match(node: Node, pred: Callable[[Any], bool]) -> bool:
    while True:
        if node is None:
            break
        if not pred(node.data):
            return False
        node = node.next
    return True


