# LeetCode 146: LRU Cache

## Overview

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache with O(1) time complexity for both get and put operations.

## Problem Description

Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity
- `int get(int key)` Return the value of the key if exists, otherwise return -1
- `void put(int key, int value)` Update the value or add the key-value pair. When the cache reaches capacity, evict the least recently used key before inserting a new item.

**Example:**
```
LRUCache cache = new LRUCache(2);
cache.put(1, 1);           // cache: {1=1}
cache.put(2, 2);           // cache: {1=1, 2=2}
cache.get(1);              // returns 1, cache: {2=2, 1=1}
cache.put(3, 3);           // evicts key 2, cache: {1=1, 3=3}
cache.get(2);              // returns -1 (not found)
cache.put(4, 4);           // evicts key 1, cache: {3=3, 4=4}
cache.get(1);              // returns -1 (not found)
cache.get(3);              // returns 3, cache: {4=4, 3=3}
cache.get(4);              // returns 4, cache: {3=3, 4=4}
```

## Algorithm

**OrderedDict Approach**:

Python's `OrderedDict` maintains insertion order and provides:
- `move_to_end(key)` - O(1) move key to end (mark as recently used)
- `popitem(last=False)` - O(1) remove first item (least recently used)

**Key Operations:**
- **get**: If key exists, move to end and return value
- **put**: If key exists, move to end. Set value. If over capacity, pop first item.

## Complexity Analysis

- **Time Complexity:** O(1) for both `get` and `put`
- **Space Complexity:** O(capacity) - stores up to capacity items

## Key Concepts

- **Hash Map**: O(1) key lookup
- **Doubly Linked List**: O(1) insertion/deletion at both ends
- **OrderedDict**: Python's built-in combination of both

## Implementation Details

### OrderedDict Operations
```python
self.cache.move_to_end(key)      # Move to "most recently used" end
self.cache.popitem(last=False)   # Remove "least recently used" (first)
```

### Order Representation
```
OrderedDict: {LRU ... ... ... MRU}
              ↑                 ↑
          First item        Last item
          (popitem)         (move_to_end)
```

## Alternative: Manual Doubly Linked List

For interviews, you might need to implement without `OrderedDict`:

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)
        return node.val
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_end(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
```

## Pattern Recognition

This problem demonstrates:
- Cache design pattern
- Hash Map + Doubly Linked List combination
- O(1) constraint satisfaction

## Related Problems

- LFU Cache (LeetCode 460)
- Design HashMap (LeetCode 706)
- Design Linked List (LeetCode 707)

## Edge Cases

- Capacity of 1
- Accessing same key multiple times
- Updating existing key's value
- Eviction order verification

## Files

- `solution.py`: OrderedDict implementation




