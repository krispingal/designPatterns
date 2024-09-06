from typing import Generic, TypeVar

T = TypeVar('T')
class CacheManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CacheManager, cls).__new__(cls)
            cls._instance.cache = {}
        return cls._instance

    def set(self, k: T, v) -> None:
        self.cache[k] = v

    def get(self, k: T):
        if k not in self.cache:
            raise ValueError
        return self.cache[k]

if __name__ == '__main__':
    c1 = CacheManager()
    c2 = CacheManager()
    c1.set("foo", "bar")
    assert c2.get("foo") == "bar"