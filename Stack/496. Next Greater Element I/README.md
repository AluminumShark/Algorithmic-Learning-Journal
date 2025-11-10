# LeetCode 496: Next Greater Element I

## Overview

Find the next greater element for each element in `nums1` by looking it up in `nums2` using a monotonic stack approach.

## Problem Description

The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

**Example:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for 4 is -1, for 1 is 3, and for 2 is -1.
```

## Algorithm

**Monotonic Decreasing Stack**: Build a mapping of next greater elements for all values in `nums2`, then answer queries from `nums1`.

**Key Steps:**
1. Initialize a decreasing monotonic stack and a mapping dictionary
2. Process `nums2`:
   - While stack is non-empty and current number > stack top:
     - Current number is the next greater for stack top
     - Map stack top to current number
     - Pop from stack
   - Push current number to stack
3. Answer queries: For each number in `nums1`, look up in mapping (default to -1)

## Complexity Analysis

- **Time Complexity:** O(n + m) - where n is length of nums2, m is length of nums1
  - Single pass through nums2: O(n)
  - Query each element in nums1: O(m)
- **Space Complexity:** O(n) - for stack and mapping dictionary

## Key Insight

The monotonic decreasing stack maintains elements waiting for their next greater element:
- When a larger number appears, it resolves all smaller numbers in the stack
- Remaining elements in stack have no next greater (map to -1)
- Pre-computing mapping allows O(1) query time

## Implementation Details

### Monotonic Stack Property
- Stack maintains decreasing order (top is smallest)
- Elements are popped when their next greater is found
- Unresolved elements remain in stack

### Mapping Strategy
- Build complete mapping for all elements in `nums2`
- Use dictionary for O(1) lookup during queries
- Default to -1 for elements without next greater

## Pattern Recognition

This problem demonstrates:
- Monotonic stack pattern
- Next greater/smaller element problems
- Pre-computation for efficient queries
- Two-phase approach (build mapping, answer queries)

## Use Cases

- Finding next greater/smaller elements
- Stock span problems
- Histogram area calculations
- Monotonic stack applications

## Related Problems

- Next Greater Element II (circular array)
- Next Greater Element III
- Daily Temperatures
- Largest Rectangle in Histogram

## Edge Cases

- No next greater element (return -1)
- All elements in decreasing order
- All elements in increasing order
- Duplicate values (handled by distinct arrays)

## Alternative Approaches

1. **Brute Force**: O(n × m)
   - For each element in nums1, search nums2
   - Inefficient for large inputs

2. **Hash Map with Linear Search**: O(n × m)
   - Map positions, then search forward
   - Still O(n × m) worst case

## Files

- `MonotoneStack.py`: Monotonic decreasing stack implementation

