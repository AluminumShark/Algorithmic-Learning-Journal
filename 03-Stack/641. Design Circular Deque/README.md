# LeetCode 641: Design Circular Deque

## Overview

Design a circular double-ended queue (deque) that supports insertion and deletion at both front and rear ends using a size counter to track elements.

## Problem Description

Design your implementation of the circular double-ended queue (deque).

Implement the `MyCircularDeque` class:
- `MyCircularDeque(k)`: Constructor, set the size of the deque to be k
- `insertFront(value)`: Adds an item at the front of Deque
- `insertLast(value)`: Adds an item at the rear of Deque
- `deleteFront()`: Deletes an item from the front of Deque
- `deleteLast()`: Deletes an item from the rear of Deque
- `getFront()`: Returns the front item from the Deque
- `getRear()`: Returns the last item from the Deque
- `isEmpty()`: Returns true if the deque is empty
- `isFull()`: Returns true if the deque is full

**Example:**
```
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);   // return True
myCircularDeque.insertLast(2);   // return True
myCircularDeque.insertFront(3);  // return True
myCircularDeque.insertFront(4);  // return False (deque is full)
myCircularDeque.getRear();       // return 2
myCircularDeque.isFull();        // return True
myCircularDeque.deleteLast();    // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();      // return 4
```

## Algorithm

**Circular Buffer with Size Counter**: Use an array of size `k` and a `size` variable to track the number of elements.

**Key Design:**
- Allocate exactly `k` spaces
- `front`: Points to the front element
- `rear`: Points to the next insertion position at rear
- `size`: Tracks current number of elements
- Empty: `size == 0`
- Full: `size == capacity`

**Key Steps:**

1. **Insert Front**:
   - Check if full
   - Move `front` backward: `front = (front - 1) % capacity`
   - Insert value at `queue[front]`
   - Increment `size`

2. **Insert Last**:
   - Check if full
   - Insert value at `queue[rear]`
   - Move `rear` forward: `rear = (rear + 1) % capacity`
   - Increment `size`

3. **Delete Front**:
   - Check if empty
   - Move `front` forward: `front = (front + 1) % capacity`
   - Decrement `size`

4. **Delete Last**:
   - Check if empty
   - Move `rear` backward: `rear = (rear - 1) % capacity`
   - Decrement `size`

5. **Get Front/Rear**:
   - Front: `queue[front]`
   - Rear: `queue[(rear - 1) % capacity]`

## Complexity Analysis

- **Time Complexity:** O(1) - all operations are constant time
- **Space Complexity:** O(k) - array of size k

## Key Insight

Deque (double-ended queue) supports operations at both ends:
- **Front operations**: Insert/delete at the beginning
- **Rear operations**: Insert/delete at the end
- Requires careful pointer management for both directions

## Implementation Details

### Size Counter Approach
- Use `size` variable to track elements
- Simplifies full/empty detection
- No need for extra space

### Circular Indexing
- Forward: `(index + 1) % capacity`
- Backward: `(index - 1) % capacity`
- Handles negative indices correctly in Python

### Pointer Management
- `front`: Points to actual front element
- `rear`: Points to next insertion position (one ahead)
- Both can move in both directions

## Pattern Recognition

This problem demonstrates:
- Double-ended queue (deque) implementation
- Circular buffer with bidirectional operations
- Size-based state tracking
- Modulo arithmetic for circular indexing

## Use Cases

- Sliding window algorithms
- Palindrome checking
- BFS with bidirectional search
- Task scheduling
- Data stream processing

## Comparison: Queue vs Deque

| Feature | Queue | Deque |
|---------|-------|-------|
| Insert | Rear only | Both ends |
| Delete | Front only | Both ends |
| Access | Front/Rear | Front/Rear |
| Use Cases | FIFO operations | Flexible operations |

## Related Problems

- Design Circular Queue (single-ended)
- Sliding Window Maximum
- Design Hit Counter

## Edge Cases

- Empty deque operations
- Full deque insertion attempts
- Single element deque
- Alternating front/rear operations

## Alternative Implementation

Using extra space approach (like Circular Queue):
- Allocate `k + 1` spaces
- Keep one space unused
- More complex pointer management for deque

## Files

- `CircularQueue.py`: Circular deque with size counter approach

