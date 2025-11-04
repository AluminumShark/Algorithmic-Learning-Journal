# LeetCode 707: Design Linked List

## Overview

Design and implement a linked list with complete CRUD operations, supporting both singly and doubly linked list implementations.

## Problem Description

Design your implementation of the linked list. You can choose to use a singly or doubly linked list. A node in a singly linked list should have two attributes: `val` and `next`. A node in a doubly linked list should have three attributes: `val`, `prev`, and `next`.

You should implement the following functions:
- `get(index)`: Get the value of the index-th node
- `addAtHead(val)`: Add a node of value val before the first element
- `addAtTail(val)`: Append a node of value val to the last element
- `addAtIndex(index, val)`: Add a node of value val before the index-th node
- `deleteAtIndex(index)`: Delete the index-th node

**Example:**
```
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);
linkedList.get(1);            // returns 3
```

## Implementations

### Singly Linked List

**Features:**
- Dummy head node (sentinel) to simplify edge cases
- Size tracking for efficient validation
- O(n) access by index

**Key Design:**
- Sentinel node eliminates special cases for head operations
- All operations unified through `addAtIndex` and `deleteAtIndex`

**Complexity:**
- Access: O(n)
- Insert at head: O(1)
- Insert at tail: O(n)
- Delete: O(n)

### Doubly Linked List

**Features:**
- Both dummy head and tail nodes (sentinels)
- Bidirectional traversal optimization
- Can choose traversal direction based on index position

**Key Design:**
- Two sentinels simplify both head and tail operations
- `_node_at()` helper chooses optimal traversal direction
- O(min(index, size - index)) for indexed access

**Complexity:**
- Access: O(min(index, size - index))
- Insert at head: O(1)
- Insert at tail: O(1)
- Delete: O(min(index, size - index))

## Algorithm Details

### Sentinel Node Pattern

**Singly Linked List:**
- Dummy head node (value 0, not counted in size)
- Real nodes start at `head.next`
- Simplifies insert/delete at index 0

**Doubly Linked List:**
- Dummy head and tail nodes
- Real nodes between `head.next` and `tail.prev`
- Simplifies all edge cases uniformly

### Index Access Optimization

**Doubly Linked List Optimization:**
```python
if index < self.size // 2:
    # Traverse from head (forward)
else:
    # Traverse from tail (backward)
```
This reduces average traversal steps by choosing the shorter path.

## Complexity Analysis

### Singly Linked List
- **Time Complexity:**
  - `get(index)`: O(n)
  - `addAtHead(val)`: O(1)
  - `addAtTail(val)`: O(n)
  - `addAtIndex(index, val)`: O(n)
  - `deleteAtIndex(index)`: O(n)
- **Space Complexity:** O(n) - for storing nodes

### Doubly Linked List
- **Time Complexity:**
  - `get(index)`: O(min(index, size - index))
  - `addAtHead(val)`: O(1)
  - `addAtTail(val)`: O(1)
  - `addAtIndex(index, val)`: O(min(index, size - index))
  - `deleteAtIndex(index)`: O(min(index, size - index))
- **Space Complexity:** O(n) - for storing nodes (slightly more due to prev pointers)

## Implementation Highlights

### Edge Case Handling
- Invalid index validation
- Negative index normalization
- Index beyond size handling
- Empty list operations

### Code Quality
- Type hints for clarity
- Comprehensive docstrings
- Consistent naming conventions
- Helper methods for code reuse

## Pattern Recognition

This problem demonstrates:
- Sentinel node pattern for simplifying edge cases
- Design choices between singly and doubly linked lists
- Trade-offs between memory and time complexity
- Unified operation design through helper methods

## Use Cases

- Understanding linked list fundamentals
- Data structure design patterns
- Pointer manipulation techniques
- Performance optimization strategies

## Comparison: Singly vs Doubly

| Aspect | Singly Linked List | Doubly Linked List |
|--------|-------------------|-------------------|
| Memory | Lower (1 pointer/node) | Higher (2 pointers/node) |
| Traversal | Forward only | Bidirectional |
| Access | O(n) always | O(min(i, n-i)) optimized |
| Tail ops | O(n) | O(1) |
| Complexity | Simpler | More complex |

## Files

- `SinglyLinkList.py`: Singly linked list with dummy head implementation
- `DoublyLinkLIst.py`: Doubly linked list with dummy head and tail implementation

