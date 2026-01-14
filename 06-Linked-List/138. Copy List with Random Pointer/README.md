# LeetCode 138: Copy List with Random Pointer

## Overview

Create a deep copy of a linked list where each node has an additional random pointer that could point to any node in the list or null.

## Problem Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.

**Example:**
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

## Algorithm

### Solution 1: Hash Map (Two Passes)

**Key Steps:**
1. **First Pass**: Create copy nodes and store mapping `{original -> copy}` in hash map
2. **Second Pass**: Set `next` and `random` pointers using the hash map lookup

### Solution 2: Interweaving / Space Optimized (Three Passes)

**Key Steps:**
1. **Interweave**: Insert copy nodes between original nodes (A->A'->B->B'->...)
2. **Set Random**: Use interweaved structure to set random pointers
3. **Separate**: Extract copy list while restoring original list

## Complexity Analysis

### Solution 1: Hash Map
- **Time Complexity:** O(n) - two passes through the list
- **Space Complexity:** O(n) - hash map stores n mappings

### Solution 2: Interweaving
- **Time Complexity:** O(n) - three passes through the list
- **Space Complexity:** O(1) - no extra space (excluding result)

## Key Concepts

### Solution 1: Hash Map Approach

The hash map stores the mapping from original nodes to copy nodes:

```python
mp = {None: None}  # Handle null random pointers
cur = head
while cur:
    mp[cur] = Node(cur.val)  # Create copy
    cur = cur.next
```

Then use the map to set pointers:
```python
mp[cur].next = mp[cur.next]      # Copy's next = copy of original's next
mp[cur].random = mp[cur.random]  # Copy's random = copy of original's random
```

### Solution 2: Interweaving Approach

**Step 1 - Interweave nodes:**
```
Original: A -> B -> C
After:    A -> A' -> B -> B' -> C -> C'
```

**Step 2 - Set random pointers:**
```python
copy.random = cur.random.next if cur.random else None
```
Since copy is right after original, `cur.random.next` is the copy of `cur.random`.

**Step 3 - Separate lists:**
```
A -> A' -> B -> B' -> C -> C'
        v
Original: A -> B -> C
Copy:     A' -> B' -> C'
```

### Visual Example (Interweaving)

```
Original list:
7 -> 13 -> 11 -> 10 -> 1
v    v     v     v    v
N    7    10    11    7   (random pointers)

Step 1 - Interweave:
7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'

Step 2 - Set random (using interweaved structure):
7'.random = 7.random.next = None (7.random is null)
13'.random = 13.random.next = 7' (13.random is 7, so 7.next is 7')
11'.random = 11.random.next = 10'
10'.random = 10.random.next = 11'
1'.random = 1.random.next = 7'

Step 3 - Separate:
Original: 7 -> 13 -> 11 -> 10 -> 1
Copy:     7' -> 13' -> 11' -> 10' -> 1' (with correct random pointers)
```

## Implementation Details

### Hash Map Approach
- `mp = {None: None}`: Handles null random pointers elegantly
- Two clean passes: create nodes, then link them
- Simple and intuitive

### Interweaving Approach
- No extra data structure needed
- Uses list structure itself as the "map"
- More complex but space-efficient
- Must restore original list structure

## Pattern Recognition

This problem demonstrates:
- Deep copy of complex data structures
- Hash map for node mapping
- Interweaving technique for O(1) space
- Handling multiple pointer types

## Use Cases

- Deep copying complex linked structures
- Cloning graphs with back edges
- Serialization/deserialization patterns

## Related Problems

- Clone Graph (LeetCode 133)
- Copy List with Random Pointer II
- Deep copy problems

## Edge Cases

- Empty list
- Single node with random pointing to itself
- All random pointers are null
- All random pointers point to same node

## Files

- `solution.py`: Both Hash Map and Interweaving solutions

