class LRUCache:

    def __init__(self, capacity: int):
        self.map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self.map.get(key):
            return -1
        self.map.move_to_end(key)
        return self.map.get(key)
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.move_to_end(key)
        self.map[key] = value
        if len(self.map) > self.capacity:
            self.map.popitem(last=False)
