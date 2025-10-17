from typing import Any
from nodes import Node

class LinkedList:

    def __init__(self, data: Any) -> None:
        self.head = Node(data)

    def __repr__(self) -> str:
        representation = ''
        current = self.getHead()
        while current:
            representation += f'{current.getData()} -> '
            current = current.getNext()
        return representation[:-4]
    
    def getHead(self) -> Node|None:
        return self.head
    
    def insert(self, data: Any) -> None:
        self.head = Node(data, self.head)

    def remove(self, toRemove) -> None:
        current = self.getHead()
        if current and current.getData() == toRemove: self.head = current.getNext()
        else:
            while current:
                nextNode = current.getNext()
                if nextNode and nextNode.getData() == toRemove:
                    current.setNext(nextNode.getNext())
                    current = None
                else: current = nextNode
        
if __name__ == '__main__':
    ll = LinkedList('c')
    ll.insert('b')
    ll.insert('d')
    ll.insert('a')
    print(ll)
    ll.remove('d')
    print(ll)