from typing import Any
from nodes import Node

class HashMap:
    
    def __init__(self, size: int) -> None:
        self.size = size
        self.array = [None] * size

    def compressedHash(self, key: str, collisions: int = 0) -> int:
        code = sum(key.encode())
        return (code + collisions) % self.size
    
    def assign(self, key: str, value: Any) -> None:
        idx = self.compressedHash(key)
        val = self.array[idx]
        if val is None:
            self.array[idx] = [key, value] # type: ignore
        
        elif val[0] == key:
            self.array[idx] = [key, value] # type: ignore

        else:
            collisions = 1
            while val[0] != key and not collisions == self.size:
                idx = self.compressedHash(key, collisions)
                val = self.array[idx]

                if val is None:
                    self.array[idx] = [key, value] # type: ignore
                    return

                elif val[0] == key:
                    self.array[idx] = [key, value] # type: ignore
                    return
                
                else:
                    collisions += 1

    def retrieve(self, key: str) -> Any:
        idx = self.compressedHash(key)
        val = self.array[idx]

        if val is None:
            return None
        
        elif val[0] == key:
            return val[1]
        
        else:
            collisions = 1
            while val[0] != key and not collisions == self.size:
                idx = self.compressedHash(key)
                val = self.array[idx]

                if val is None:
                    return None
                
                elif val[0] == key:
                    return val[1]
                
                else:
                    collisions += 1

if __name__ == '__main__':
    h = HashMap(3)
    h.assign('a', 1)
    h.assign('b', 2)
    h.assign('c', 3)
    print(h.retrieve('c'))
    h.assign('c', 4)
    print(h.retrieve('c'))