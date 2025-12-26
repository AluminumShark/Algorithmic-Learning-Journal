# LeetCode 141: Linked List Cycle

## Overview

Detect if a linked list has a cycle using Floyd's Tortoise and Hare algorithm (slow/fast pointers).

## Problem Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Algorithm

**Floyd's Tortoise and Hare**: Use two pointers moving at different speeds. If there's a cycle, they will eventually meet.

**Key Steps:**
1. Initialize slow pointer `S` and fast pointer `F` at head
2. While `F` and `F.next` exist:
   - Move slow pointer one step: `S = S.next`
   - Move fast pointer two steps: `F = F.next.next`
   - If `S == F`: Cycle detected, return `True`
3. If loop ends (fast reaches null): No cycle, return `False`

## Complexity Analysis

- **Time Complexity:** O(n) - at most n iterations before cycle detection or list end
- **Space Complexity:** O(1) - only uses two pointers regardless of list size

## Key Concepts

### Floyd's Cycle Detection Algorithm

Also known as the "Tortoise and Hare" algorithm:

- **Slow pointer (Tortoise)**: Moves one step at a time
- **Fast pointer (Hare)**: Moves two steps at a time

**Why does this work?**

1. **If no cycle**: Fast pointer reaches the end (null), loop terminates
2. **If cycle exists**: 
   - Both pointers enter the cycle
   - Fast pointer gains on slow pointer by 1 position per iteration
   - They will eventually meet inside the cycle

### Mathematical Intuition

When both pointers are in a cycle of length `L`:
- Relative speed of fast to slow = 1 step per iteration
- Distance between them decreases by 1 each iteration
- They meet after at most `L` iterations inside the cycle

### Visual Example

```
List with cycle:  3 -> 2 -> 0 -> -4
                       ↑         |
                       └─────────┘

Step 0: S=3, F=3
Step 1: S=2, F=0
Step 2: S=0, F=2 (F went -4 -> 2)
Step 3: S=-4, F=-4
S == F → Cycle detected!
```

## Implementation Details

- Check `F and F.next` to prevent null pointer errors
- Compare pointers (not values) to detect meeting point
- Both pointers start at head (allows immediate cycle detection for self-loops)

## Alternative Approaches

### Hash Set Approach
```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
```
- **Time:** O(n)
- **Space:** O(n) - stores all visited nodes

Floyd's approach is superior for space efficiency.

## Pattern Recognition

This problem demonstrates:
- Floyd's cycle detection algorithm
- Slow/fast pointer technique
- Constant space linked list analysis
- Foundational cycle detection pattern

## Use Cases

- Cycle detection in linked structures
- Infinite loop detection
- Finding cycle start point (extended problem)
- Memory leak detection in data structures

## Related Problems

- Linked List Cycle II (LeetCode 142) - find cycle start
- Find the Duplicate Number (LeetCode 287)
- Happy Number (LeetCode 202) - cycle in number sequence
- Circular Array Loop (LeetCode 457)

## Edge Cases

- Empty list (`head = None`)
- Single node without cycle
- Single node with self-loop
- Cycle at the beginning vs middle

## Files

- `solution.py`: Floyd's Tortoise and Hare implementation

