# LeetCode 153: Find Minimum in Rotated Sorted Array

## Overview

Find the minimum element in a rotated sorted array using binary search, where the array was rotated at an unknown pivot point.

## Problem Description

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

**Example:**
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The array was rotated 0 times (or n times).
```

## Algorithm

**Binary Search (Compare with Right Boundary)**: Use binary search to locate the pivot point where the minimum element resides.

**Key Steps:**
1. Initialize `left = 0` and `right = len(nums) - 1`
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`
   - Compare `nums[mid]` with `nums[right]`:
     - If `nums[mid] > nums[right]`: Minimum is in right half, set `left = mid + 1`
     - Else: Minimum is in left half (including mid), set `right = mid`
3. Return `nums[left]` (or `nums[right]`, they converge)

## Complexity Analysis

- **Time Complexity:** O(log n) - binary search halves search space each iteration
- **Space Complexity:** O(1) - only uses constant extra space

## Key Concepts

### Why Compare `nums[mid]` with `nums[right]`?

This is a critical design choice that determines which side of the rotation pivot we are on. Here's the detailed explanation:

**Understanding the Rotated Array Structure:**

A rotated sorted array has two sorted segments separated by a pivot point:
- **Left segment**: Values from the original end of the array (larger values)
- **Right segment**: Values from the original beginning (smaller values, including minimum)

Example: `[4,5,6,7,0,1,2]`
- Left segment: `[4,5,6,7]` (larger values)
- Right segment: `[0,1,2]` (smaller values, minimum = 0)
- Pivot point: between 7 and 0

**Why Right Boundary Instead of Left?**

1. **Determining Pivot Location:**
   - If `nums[mid] > nums[right]`: 
     - This means `mid` is in the **left segment** (larger values)
     - The pivot (minimum) must be to the **right** of `mid`
     - Example: `nums[mid]=6, nums[right]=2` → mid is in [4,5,6,7], min is in [0,1,2]
     - Action: `left = mid + 1` (search right)

   - If `nums[mid] ≤ nums[right]`:
     - This means `mid` is in the **right segment** (smaller values)
     - The pivot (minimum) is at `mid` or to the **left** of `mid`
     - Example: `nums[mid]=1, nums[right]=2` → mid is in [0,1,2], min could be 0 or 1
     - Action: `right = mid` (search left, keep mid as candidate)

2. **Why Not Compare with Left Boundary?**
   - Comparing with `nums[left]` is ambiguous:
     - If `nums[mid] > nums[left]`: Could mean mid is in left segment OR array is not rotated
     - If `nums[mid] < nums[left]`: Could mean mid is in right segment OR array is not rotated
   - The right boundary provides clearer information about which segment we're in

3. **Edge Case Handling:**
   - When array is not rotated: `nums[mid] ≤ nums[right]` always true, correctly converges to left
   - When mid equals minimum: `nums[mid] ≤ nums[right]`, we keep mid as candidate (`right = mid`)

**Visual Example:**

```
Array: [4,5,6,7,0,1,2]
        L     M     R

nums[mid] = 6, nums[right] = 2
6 > 2 → mid is in left segment [4,5,6,7]
→ Minimum must be in [0,1,2] (right of mid)
→ left = mid + 1

Array: [4,5,6,7,0,1,2]
              L M   R

nums[mid] = 1, nums[right] = 2
1 ≤ 2 → mid is in right segment [0,1,2]
→ Minimum is at mid or left of mid
→ right = mid (keep mid as candidate)
```

## Implementation Details

- **Loop Condition**: `left < right` (not `≤`) ensures convergence
- **Boundary Updates**:
  - When `nums[mid] > nums[right]`: Exclude mid (`left = mid + 1`)
  - When `nums[mid] ≤ nums[right]`: Keep mid (`right = mid`)
- **Termination**: When `left == right`, we've found the minimum
- **No Overflow**: Uses `(left + right) // 2` (safe for Python, but good practice)

## Pattern Recognition

This problem demonstrates:
- Binary search on rotated arrays
- Finding pivot points in rotated structures
- Comparing with boundary elements to determine search direction
- Handling edge cases (no rotation, single element)

## Use Cases

- Finding pivot points in rotated data structures
- Search in rotated sorted arrays
- Understanding binary search variations
- Array rotation problems

## Related Problems

- Search in Rotated Sorted Array (LeetCode 33)
- Find Minimum in Rotated Sorted Array II (LeetCode 154) - with duplicates
- Search in Rotated Sorted Array II (LeetCode 81)
- Binary search on rotated arrays

## Edge Cases

- Array not rotated (sorted normally)
- Array rotated n times (back to original)
- Single element array
- Two element array
- Minimum at different positions

## Files

- `solution.py`: Binary Search implementation comparing with right boundary

