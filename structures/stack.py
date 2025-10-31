from nodes import Node
from typing import Any

class Stack:

    def __init__(self, maxSize: int|None = None) -> None:
        self.top = None
        self.size = 0
        self.maxSize = maxSize

    def __len__(self) -> int:
        return self.size

    def push(self, data: Any) -> None:
        if self.hasSpace():
            toPush = Node(data)
            toPush.setNext(self.top)
            self.top = toPush
            self.size += 1

    def pop(self) -> Any:
        if not self.isEmpty():
            toRemove = self.top
            self.top = toRemove.getNext() # type: ignore
            self.size -= 1
            return toRemove.getData() # type: ignore

    def peek(self) -> Any:
        if not self.isEmpty(): return self.top.getData() # type: ignore

    def hasSpace(self) -> bool:
        return self.maxSize is None or self.maxSize > len(self)

    def isEmpty(self) -> bool:
        return len(self) == 0
    

if __name__ == '__main__':
    stack = Stack(3)
    stack.push('a')
    stack.push('b')
    print(stack.peek())
    stack.push('c')
    stack.push('d')
    print(stack.pop())