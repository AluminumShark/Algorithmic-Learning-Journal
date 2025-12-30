# LeetCode 2: Add Two Numbers

## Overview

Add two numbers represented as linked lists in reverse order, returning the sum as a linked list.

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Example:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Algorithm

**Math Simulation with Carry**:

**Key Steps:**
1. Use dummy node to simplify list construction
2. Iterate while either list has nodes OR carry exists
3. Sum values from both lists (use 0 if null) plus carry
4. Create new node with `sum % 10`
5. Update carry as `sum // 10`
6. Move pointers forward

## Complexity Analysis

- **Time Complexity:** O(max(m, n)) - traverse both lists once
- **Space Complexity:** O(max(m, n)) - result list length

## Key Concepts

- **Dummy Node**: Simplifies head handling
- **Carry Propagation**: Handle overflow between digits
- **Reverse Order Advantage**: Can process from least significant digit

## Implementation Details

### Why Reverse Order Helps
Numbers stored in reverse order allows direct addition:
```
  342 stored as: 2 -> 4 -> 3
+ 465 stored as: 5 -> 6 -> 4
= 807 stored as: 7 -> 0 -> 8
```
We add from left to right (least significant first), which is natural for carry propagation.

### Handle Different Lengths
```python
x = l1.val if l1 else 0
y = l2.val if l2 else 0
```
Use 0 when one list is shorter than the other.

### Don't Forget Final Carry
```python
while l1 or l2 or carry:  # Include carry in condition
```
Example: 99 + 1 = 100 (carry creates extra digit)

## Pattern Recognition

This problem demonstrates:
- Linked list traversal and construction
- Math simulation with carry
- Dummy node pattern

## Related Problems

- Add Two Numbers II (LeetCode 445) - digits in normal order
- Plus One (LeetCode 66)
- Add Binary (LeetCode 67)
- Multiply Strings (LeetCode 43)

## Edge Cases

- Different length lists
- Carry at the end (9 + 1 = 10)
- Single digit numbers
- Large numbers with many carries

## Files

- `solution.py`: Math simulation implementation

