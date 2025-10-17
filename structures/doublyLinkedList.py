from typing import Any
from nodes import Node

class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        representation = ''
        current = self.head
        while current:
            representation += f'{current.getData()} <-> '
            current = current.getNext()
        return representation[:-5]
    
    def getHead(self) -> Node|None:
        return self.head
    
    def getTail(self) -> Node|None:
        return self.tail

    def appendLeft(self, data: Any) -> None:
        oldHead = self.getHead()
        self.head = Node(data)
        if oldHead: oldHead.setPrev(self.head)
        self.head.setNext(oldHead)
        if not self.tail: self.tail = self.head

    def popLeft(self) -> Node|None:
        oldHead = self.getHead()
        if not oldHead: return None
        
        self.head = oldHead.getNext()
        if self.head: self.head.setPrev(None)
        if oldHead == self.tail: self.pop()

        return oldHead.getData()

    def append(self, data: Any) -> None:
        oldTail = self.getTail()
        self.tail = Node(data)
        if oldTail: oldTail.setNext(self.tail)
        self.tail.setPrev(oldTail)
        if not self.head: self.head = self.tail

    def pop(self, toRemove: Any = None) -> Node|None:
        if toRemove is None:
            oldTail = self.getTail()
            if not oldTail: return None
            
            self.tail = oldTail.getPrev()
            if self.tail: self.tail.setNext(None)
            if oldTail == self.head: self.popLeft()

            return oldTail.getData()
        
        else:
            removed = None
            current = self.head
            while current:
                if current.getData() == toRemove:
                    removed = current
                    break
                current = current.getNext()
            if not removed: return None

            if removed == self.head: self.popLeft()
            elif removed == self.tail: self.pop()
            else:
                removed.getPrev().setNext(removed.getNext()) # type: ignore
                removed.getNext().setPrev(removed.getPrev()) # type: ignore
            
            return removed.getData()

if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.append('a')
    dl.appendLeft('d')
    dl.appendLeft('e')
    dl.append('b')
    dl.append('c')
    dl.append('f')
    print(dl)
    print(dl.pop('d'))
    print(dl.popLeft())
    print(dl.pop())
    print(dl)