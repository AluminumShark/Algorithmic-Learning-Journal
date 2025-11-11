# LeetCode 622: Design Circular Queue

## Overview

Design a circular queue implementation with fixed capacity using an array-based approach with an extra space to distinguish between full and empty states.

## Problem Description

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

**Operations:**
- `MyCircularQueue(k)`: Constructor, set the size of the queue to be k
- `enQueue(value)`: Insert an element into the circular queue
- `deQueue()`: Delete an element from the circular queue
- `Front()`: Get the front item from the queue
- `Rear()`: Get the last item from the queue
- `isEmpty()`: Checks whether the circular queue is empty
- `isFull()`: Checks whether the circular queue is full

**Example:**
```
MyCircularQueue circularQueue = new MyCircularQueue(3);
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false (queue is full)
circularQueue.Rear();      // return 3
circularQueue.isFull();    // return true
circularQueue.deQueue();   // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();      // return 4
```

## Algorithm

**Circular Buffer with Extra Space**: Use an array of size `k + 1` to distinguish between full and empty states.

**Key Design:**
- Allocate `k + 1` spaces (one extra) to avoid ambiguity
- `front`: Points to the position before the first element
- `rear`: Points to the last element
- Empty: `front == rear`
- Full: `(rear + 1) % capacity == front`

**Key Steps:**
1. **Enqueue**: 
   - Check if full
   - Move `rear` forward: `rear = (rear + 1) % capacity`
   - Insert value at `queue[rear]`

2. **Dequeue**:
   - Check if empty
   - Move `front` forward: `front = (front + 1) % capacity`

3. **Front/Rear Access**:
   - Front: `queue[(front + 1) % capacity]`
   - Rear: `queue[rear]`

## Complexity Analysis

- **Time Complexity:** O(1) - all operations are constant time
- **Space Complexity:** O(k) - array of size k + 1

## Key Insight

The challenge in circular queue design is distinguishing between full and empty states when `front == rear`. Solutions:

1. **Extra Space Approach** (this implementation):
   - Allocate `k + 1` spaces
   - Keep one space always unused
   - Full: `(rear + 1) % capacity == front`
   - Empty: `rear == front`

2. **Size Counter Approach**:
   - Track number of elements with `size` variable
   - Full: `size == capacity`
   - Empty: `size == 0`

## Implementation Details

### Circular Indexing
- Use modulo operation: `(index + 1) % capacity`
- Wraps around when reaching array end
- Enables circular traversal

### Front and Rear Pointers
- `front`: Points before first element (one step behind)
- `rear`: Points to last element
- This design simplifies full/empty detection

### State Detection
- **Empty**: `front == rear` (pointers coincide)
- **Full**: `(rear + 1) % capacity == front` (rear's next position is front)

## Pattern Recognition

This problem demonstrates:
- Circular buffer implementation
- FIFO queue operations
- Array-based data structure design
- Modulo arithmetic for circular indexing

## Use Cases

- Fixed-size queue requirements
- Ring buffer implementations
- Producer-consumer problems
- Sliding window algorithms
- System resource management

## Related Problems

- Design Circular Deque (supports both ends)
- Moving Average from Data Stream
- Sliding Window Maximum

## Edge Cases

- Empty queue operations
- Full queue insertion attempts
- Single element queue
- Maximum capacity operations

## Alternative Implementation

Using size counter instead of extra space:
```python
def isEmpty(self) -> bool:
    return self.size == 0

def isFull(self) -> bool:
    return self.size == self.capacity
```

## Files

- `CircularQueue.py`: Circular queue with extra space approach

