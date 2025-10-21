from nodes import Node
from typing import Any

class Queue:

    def __init__(self, maxSize: int|None = None) -> None:
        self.head = None
        self.tail = None
        self.maxSize = maxSize
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def enqueue(self, data: Any) -> None:
        if self.hasSpace():
            appended = Node(data)
            if not isinstance(self.tail, Node):
                self.head = appended
            else:
                self.tail.setNext(appended)
            self.tail = appended
            self.size += 1

    def dequeue(self) -> Any:
        if isinstance(self.head, Node):
            popped = self.head.getData()
            if len(self) == 1:
                self.head = None
                self.tail = None
            else: self.head = self.head.getNext()
            self.size -= 1
            return popped

    def peek(self) -> Any:
        if isinstance(self.head, Node):
            return self.head.getData()

    def hasSpace(self) -> bool:
        return self.maxSize is None or self.maxSize > len(self)

    def isEmpty(self) -> bool:
        return self.size == 0

if __name__ == '__main__':
    q = Queue(maxSize=3)
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    print(q.peek())
    while q.peek():
        print(q.dequeue())