# LeetCode 217: Contains Duplicate

## Overview

Determine if an array contains any duplicate elements using a hash set for efficient O(1) lookup.

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example:**
```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

## Algorithm

**Hash Set Approach**: Use a hash set (dictionary) to track seen elements and detect duplicates in a single pass.

**Key Steps:**
1. Initialize an empty hash set/dictionary
2. Iterate through each number in the array:
   - If number exists in set: return `true` (duplicate found)
   - Otherwise: add number to set
3. If loop completes: return `false` (no duplicates)

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the array, hash operations are O(1) average case
- **Space Complexity:** O(n) - hash set stores at most n elements in worst case

## Key Insight

Hash sets provide O(1) average-case lookup and insertion:
- Check existence: O(1) average
- Insert element: O(1) average
- Enables single-pass solution

## Implementation Details

### Hash Set Usage
- Dictionary in Python can be used as a set
- Key-value mapping: `numDict[num] = num`
- Existence check: `if num in numDict`

### Early Termination
- Return immediately when duplicate is found
- Avoids unnecessary iterations
- Optimizes best-case performance

## Alternative Approaches

1. **Sorting Approach**: O(n log n) time, O(1) space
   ```python
   nums.sort()
   for i in range(len(nums) - 1):
       if nums[i] == nums[i + 1]:
           return True
   return False
   ```
   - Trade-off: Better space, worse time

2. **Set Length Comparison**: O(n) time, O(n) space
   ```python
   return len(nums) != len(set(nums))
   ```
   - More Pythonic but creates full set

3. **Brute Force**: O(n²) time, O(1) space
   - Compare all pairs
   - Inefficient for large inputs

## Pattern Recognition

This problem demonstrates:
- Hash set for duplicate detection
- Single-pass algorithm design
- Early termination optimization
- Space-time trade-offs

## Use Cases

- Duplicate detection in data streams
- Data validation
- Set operations
- Frequency counting (foundation)

## Related Problems

- Contains Duplicate II (within k distance)
- Contains Duplicate III (within value and index range)
- Find All Duplicates in an Array
- Find the Duplicate Number

## Edge Cases

- Empty array (no duplicates)
- Single element (no duplicates)
- All elements same (all duplicates)
- Large array with no duplicates
- Negative numbers (handled by hash)

## Optimization Notes

- **Best Case**: O(1) - duplicate at beginning
- **Average Case**: O(n) - duplicate found midway
- **Worst Case**: O(n) - no duplicates, check all elements

## Files

- `Hash.py`: Hash set-based duplicate detection

