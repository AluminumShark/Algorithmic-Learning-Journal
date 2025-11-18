# LeetCode 876: Middle of the Linked List

## Overview

Find the middle node of a linked list using the two-pointer technique (fast and slow pointers).

## Problem Description

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes (even length), return the second middle node.

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

## Algorithm Implementations

### Two-Pointer Approach (Recommended)
**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(1)

**Key Steps:**
1. Initialize `slow` and `fast` pointers at head
2. Move `slow` one step, `fast` two steps at a time
3. When `fast` reaches the end, `slow` is at the middle
4. Return `slow`

**Why it works:**
- `fast` moves twice as fast as `slow`
- When `fast` completes n steps, `slow` completes n/2 steps
- `slow` is at the middle position

### Two-Pass Approach
**Time Complexity:** O(n) - two passes  
**Space Complexity:** O(1)

**Key Steps:**
1. First pass: count total nodes
2. Second pass: move to middle position (count // 2 steps)
3. Return the node at middle position

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Passes |
|----------|----------------|------------------|--------|
| Two-Pointer | O(n) | O(1) | 1 |
| Two-Pass | O(n) | O(1) | 2 |

## Key Insight

The two-pointer technique (tortoise and hare) is optimal:
- Single pass through the list
- No need to know list length in advance
- Constant space usage

## Implementation Details

### Two-Pointer Pattern
- `slow`: Moves one step at a time
- `fast`: Moves two steps at a time
- Loop condition: `fast and fast.next`
- When `fast` reaches end, `slow` is at middle

### Even vs Odd Length
- Odd length: `slow` at exact middle
- Even length: `slow` at second middle (as required)
- `fast.next == None` indicates odd length
- `fast == None` indicates even length

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique (fast and slow)
- Finding middle element pattern
- Single-pass optimization
- Tortoise and hare algorithm

## Use Cases

- Finding middle element in linked structures
- Merge sort on linked lists (finding split point)
- Palindrome checking (split at middle)
- List partitioning

## Related Problems

- Remove Nth Node From End of List
- Sort List (uses middle finding)
- Reorder List
- Palindrome Linked List

## Edge Cases

- Single node (return itself)
- Two nodes (return second)
- Empty list (return None)
- Odd vs even length handling

## Files

- `TwoPointers.py`: Two-pointer (fast-slow) implementation
- `OnePointer.py`: Two-pass implementation

