# LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Overview

Count the number of contiguous sub-arrays of size `k` whose average is greater than or equal to a given threshold.

## Problem Description

Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` and average greater than or equal to `threshold`.

**Example:**
```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
```

## Algorithm

**Sliding Window with Fixed Size**: Use a sliding window of size `k` to efficiently compute sub-array sums.

**Key Steps:**
1. Initialize two pointers: `slow = 0` and `fast = 0`
2. Maintain `windowSum` to track current window sum
3. Expand window by moving `fast` pointer and adding `arr[fast]` to sum
4. When window size reaches `k`:
   - Check if average (`windowSum / k`) >= `threshold`
   - If yes, increment count
   - Remove `arr[slow]` from sum and move `slow` forward (slide window)
5. Continue until `fast` reaches end of array

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the array, each element visited at most twice
- **Space Complexity:** O(1) - only uses constant extra space for pointers and variables

## Optimization

Instead of computing average each time, we can compare `windowSum >= threshold * k` to avoid floating-point division:
- More efficient: integer comparison vs. division
- Avoids floating-point precision issues
- Same logic: `sum/k >= threshold` is equivalent to `sum >= threshold * k`

## Implementation Details

- Fixed-size sliding window pattern
- Maintains window sum dynamically by adding new element and removing old element
- Window size validation: `fast - slow + 1 == k`
- Efficient: avoids recomputing sum for overlapping windows

## Pattern Recognition

This problem demonstrates:
- Fixed-size sliding window technique
- Sub-array sum computation
- Window maintenance without recalculation

## Use Cases

- Sub-array statistics (average, sum, etc.)
- Fixed-window size problems
- Performance monitoring (rolling averages)
- Data stream processing

## Related Problems

- Maximum Average Subarray I
- Subarray Sum Equals K
- Minimum Size Subarray Sum
- Other sliding window problems

## Files

- `SlidingWindowProtocol.py`: Fixed-size sliding window implementation

