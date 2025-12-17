# LeetCode 155: Min Stack

## Overview

Design a stack that supports push, pop, top, and retrieving the minimum element in constant O(1) time.

## Problem Description

Design a stack that supports the following operations:
- `push(val)` — Push element val onto stack
- `pop()` — Remove the element on top of stack
- `top()` — Get the top element
- `getMin()` — Retrieve the minimum element in the stack

All operations must be O(1) time complexity.

**Example:**
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Algorithm

**Tuple Stack Approach**: Store each element along with the current minimum at that point.

**Key Insight:**
- When we push, the minimum can only decrease or stay the same
- When we pop, we need to know what the minimum was before this element
- Solution: Store `(value, currentMin)` pairs

## Complexity Analysis

- **Time Complexity:** O(1) for all operations
- **Space Complexity:** O(n) - each element stores additional min value

## Key Concepts

- **Auxiliary Min Tracking**: Store min with each element
- **Stack Invariant**: Each entry knows the min of elements below it
- **Design Pattern**: Trade space for time

## Implementation Details

### Push Operation
```python
def push(self, val):
    if not self.stack:
        curMin = val
    else:
        curMin = min(val, self.stack[-1][1])
    self.stack.append((val, curMin))
```

### Why This Works
- Each stack entry `(val, min)` represents:
  - `val`: The actual value pushed
  - `min`: The minimum of all values from bottom to this entry
- When popping, the previous entry still has correct min

## Pattern Recognition

This problem demonstrates:
- Auxiliary data structure design
- O(1) constraint satisfaction
- Space-time trade-off

## Alternative Approaches

### Two Stack Approach
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
```
- Only pushes to minStack when new minimum found
- Slightly better space in some cases

## Related Problems

- Max Stack
- Stack with Increment Operation
- Design a Stack With Increment Operation

## Edge Cases

- Single element stack
- All elements are the same
- Monotonically increasing values
- Monotonically decreasing values
- Negative numbers

## Files

- `solution.py`: Tuple stack implementation

