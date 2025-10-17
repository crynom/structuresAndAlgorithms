from __future__ import annotations
from typing import Any

class Node:

    def __init__(self, data: Any, nextNode: Node|None = None) -> None:
        self.data = data
        self.nextNode = nextNode

    def setNext(self, nextNode) -> None:
        self.nextNode = nextNode

    def getNext(self) -> Node|None:
        return self.nextNode
    
    def getData(self) -> Any:
        return self.data
    
if __name__ == '__main__':
    # trying things out
    b, c = Node('b'), Node('c')
    a = Node('a', b)
    b.setNext(c)

    current = a
    while current:
        print(current.getData())
        current = current.getNext()

