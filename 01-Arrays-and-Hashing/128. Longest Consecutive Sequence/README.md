# LeetCode 128: Longest Consecutive Sequence

## Overview

Find the length of the longest consecutive elements sequence in an unsorted array in O(n) time.

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length = 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

## Algorithm

### Solution 1: Brute Force-ish

**Key Steps:**
1. Convert array to hash set
2. For each number, count consecutive numbers going up
3. Track maximum count found

**Issue:** May recount same sequences multiple times

### Solution 2: Optimized Set (O(n))

**Key Steps:**
1. Convert array to hash set
2. For each number, check if it's a sequence START (n-1 not in set)
3. Only count from sequence starts
4. This ensures each number is visited at most twice

## Complexity Analysis

### Solution 1: Brute Force
- **Time Complexity:** O(n²) worst case - may iterate sequence multiple times
- **Space Complexity:** O(n) - hash set storage

### Solution 2: Optimized
- **Time Complexity:** O(n) - each number visited at most twice
- **Space Complexity:** O(n) - hash set storage

## Key Concepts

- **Hash Set**: O(1) lookup for consecutive checking
- **Sequence Start Detection**: Only start from leftmost element
- **Optimization**: Avoid redundant counting

## Implementation Details

### Why Check `n - 1 not in set`?
This ensures we only start counting from the beginning of a sequence:
```
nums = [1, 2, 3, 4]
- 1: (0 not in set) → Start here, count 4
- 2: (1 in set) → Skip (not a start)
- 3: (2 in set) → Skip
- 4: (3 in set) → Skip
```

### Time Complexity Proof
- Each number is visited once in the outer loop
- Each number is visited at most once in inner while loop
- Total: O(2n) = O(n)

## Pattern Recognition

This problem demonstrates:
- Hash set for O(1) lookups
- Sequence detection pattern
- Optimization through intelligent iteration

## Alternative Approaches

### Sorting Approach
```python
def longestConsecutive(self, nums):
    if not nums:
        return 0
    nums.sort()
    longest, current = 1, 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
    return max(longest, current)
```
- Time: O(n log n), Space: O(1) or O(n)

## Related Problems

- Longest Consecutive Sequence II (Binary Tree)
- Binary Tree Longest Consecutive Sequence
- Arithmetic Slices

## Edge Cases

- Empty array
- Single element
- All elements are the same
- No consecutive sequences (all isolated)
- Negative numbers
- Duplicate elements

## Files

- `solution.py`: Brute Force and Optimized implementations

