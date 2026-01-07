from collections import OrderedDict

class LRUCache:
    """
    LRU Cache Implementation using OrderedDict
    
    Time: O(1) for both get and put
    Space: O(capacity)
    
    Concept: Combined Hash Map + Doubly Linked List (via Python's OrderedDict).
    - move_to_end() handles "Recently Used" update.
    - popitem(last=False) handles removing the "Least Recently Used" (first item).
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Mark as recently used by moving to end
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # Evict LRU (first item) if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)






