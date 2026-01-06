# LeetCode 287: Find the Duplicate Number

## Overview

Find the duplicate number in an array of n+1 integers where each integer is in range [1, n], using Floyd's Cycle Detection algorithm for O(1) space.

## Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array and using only constant extra space.

**Example:**
```
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3
```

## Algorithm

### Solution 1: Floyd's Cycle Detection

**Key Insight:** Treat the array as a linked list where `index i` points to `nums[i]`.

Since there's a duplicate, two indices point to the same value, creating a cycle.

**Phase 1: Find Intersection**
- Use slow (1 step) and fast (2 steps) pointers
- They will meet inside the cycle

**Phase 2: Find Cycle Entrance**
- Reset one pointer to start
- Move both at same speed
- They meet at the duplicate number

### Solution 2: Hash Set

Simply track seen numbers and return when duplicate found.

## Complexity Analysis

### Solution 1: Floyd's Cycle Detection
- **Time Complexity:** O(n) - linear traversal
- **Space Complexity:** O(1) - only pointers

### Solution 2: Hash Set
- **Time Complexity:** O(n) - single pass
- **Space Complexity:** O(n) - set storage

## Key Concepts

- **Array as Linked List**: `nums[i]` represents "next pointer"
- **Floyd's Algorithm**: Cycle detection in linked structures
- **Two-Phase Approach**: Find intersection, then find entrance

## Implementation Details

### Why Array Can Be Seen as Linked List
```
nums = [1, 3, 4, 2, 2]
index:  0  1  2  3  4

0 -> nums[0] = 1
1 -> nums[1] = 3
3 -> nums[3] = 2
2 -> nums[2] = 4
4 -> nums[4] = 2  <- cycle! (back to index 2)

Path: 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ...
                     ↑__________|
                     (cycle at duplicate value 2)
```

### Why Floyd's Algorithm Works
The duplicate number is the entrance to the cycle:
- Multiple indices point to the same value (the duplicate)
- This creates a cycle when following "next pointers"

## Pattern Recognition

This problem demonstrates:
- Floyd's Tortoise and Hare algorithm
- Array-to-linked-list transformation
- Space optimization techniques

## Related Problems

- Linked List Cycle (LeetCode 141)
- Linked List Cycle II (LeetCode 142)
- Happy Number (LeetCode 202) - also uses cycle detection

## Edge Cases

- Duplicate at the beginning
- Duplicate at the end
- All same values
- Only two elements

## Files

- `solution.py`: Floyd's Cycle Detection and Hash Set implementations




