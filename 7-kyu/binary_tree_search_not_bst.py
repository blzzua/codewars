# https://www.codewars.com/kata/5acc79efc6fde7838a0000a0

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right
        
    
def search(n: int, root: Optional[Node]) -> bool:
    if root is None:
        return False
    if root.value == n:
        return True
    else:
        if search(n, root.left):
            return True
        elif search(n, root.right):
            return True            
        return False


