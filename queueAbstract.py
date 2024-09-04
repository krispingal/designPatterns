from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypeVar, Generic

T = TypeVar('T')


class QueueABC(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, v: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

@dataclass
class QueueImpl(QueueABC, Generic[T]):
    _items: list[T] = field(default_factory=list)
    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if self.is_empty(): raise IndexError
        # The following is an O(n) operation
        return self._items.pop(0)

    def is_empty(self) -> bool:
        return not self._items

    def peek(self) -> T:
        if self.is_empty(): raise IndexError
        return self._items[0]

    def __len__(self):
        return len(self._items)

if __name__ == '__main__':
    q = QueueImpl()
    s = "All that is gold does not glitter"
    for w in s.split():
        q.enqueue(w)
    print(q)
    while len(q):
        print(q.dequeue())
