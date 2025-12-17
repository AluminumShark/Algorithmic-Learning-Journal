# LeetCode 167: Two Sum II - Input Array Is Sorted

## Overview

Find two numbers in a sorted array that add up to a specific target, using 1-indexed positions.

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

**Example:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
```

## Algorithm

**Two Pointers from Ends**: Start with pointers at both ends and move them inward based on sum comparison.

**Key Steps:**
1. Initialize `left = 0` and `right = len(numbers) - 1`
2. Calculate `current_sum = numbers[left] + numbers[right]`
3. Compare with target:
   - If `current_sum == target`: return indices (1-indexed)
   - If `current_sum < target`: move `left` rightward (need larger sum)
   - If `current_sum > target`: move `right` leftward (need smaller sum)
4. Continue until solution is found

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(1) - only uses constant extra space for pointers

## Why This Works

Because the array is sorted:
- Moving `left` right increases the sum
- Moving `right` left decreases the sum
- This guarantees finding the solution if it exists

## Alternative Approaches

1. **Hash Map**: O(n) time, O(n) space
   - Works for unsorted arrays
   - More space overhead

2. **Binary Search**: O(n log n) time
   - For each element, binary search for complement
   - Less efficient than two pointers

## Implementation Details

- Returns 1-indexed positions as per problem requirement
- Utilizes sorted property for efficient search
- Single pass algorithm

## Pattern Recognition

This problem demonstrates:
- Two-pointer technique on sorted arrays
- Sum-based search patterns
- Leveraging sorted property for optimization

## Use Cases

- Finding pairs with specific sum
- Pair searching in sorted data
- Two-sum variations
- Foundation for three-sum and four-sum problems

## Related Problems

- Two Sum (unsorted array)
- Three Sum
- Four Sum

## Files

- `TwoPointers.py`: Two-pointer from ends implementation

