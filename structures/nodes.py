from typing import Any

class Node:

    def __init__(self, data: type[Any], nextNode = None) -> None:
        self.data = data
        self.nextNode = nextNode

    def setNext(self, nextNode) -> None:
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode
    
    def getData(self) -> type:
        return self.data
    
if __name__ == '__main__':
    # trying things out
    b, c = Node('b'), Node('c')
    a = Node('a', b)
    b.setNext(c)

    current = a
    while True:
        print(current.getData())
        if not current.getNext(): break
        current = current.getNext()

