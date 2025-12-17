# LeetCode 238: Product of Array Except Self

## Overview

Calculate the product of all elements except the current element without using division, using prefix and postfix products.

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and **without using division**.

**Example:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2*3*4 = 24
- answer[1] = 1*3*4 = 12
- answer[2] = 1*2*4 = 8
- answer[3] = 1*2*3 = 6
```

## Algorithm

### Solution 1: Prefix & Postfix Arrays

**Key Steps:**
1. Build prefix array: `prefix[i] = product of nums[0..i]`
2. Build postfix array: `postfix[i] = product of nums[i..n-1]`
3. For each index i: `ans[i] = prefix[i-1] * postfix[i+1]`
4. Handle edge cases for first and last elements

### Solution 2: O(1) Space Optimization

**Key Steps:**
1. Use output array to store prefix products
2. Second pass: multiply with running postfix product
3. Avoids separate prefix/postfix arrays

## Complexity Analysis

### Solution 1: Prefix & Postfix Arrays
- **Time Complexity:** O(n) - three passes through the array
- **Space Complexity:** O(n) - prefix and postfix arrays

### Solution 2: Space Optimized
- **Time Complexity:** O(n) - two passes through the array
- **Space Complexity:** O(1) - only output array (not counted as extra space)

## Key Concepts

- **Prefix/Suffix Products**: Precompute cumulative products
- **No Division**: Uses multiplication only
- **Space Optimization**: Reuse output array for computation

## Implementation Details

### Prefix Array
```
nums:   [1, 2, 3, 4]
prefix: [1, 2, 6, 24]
```

### Postfix Array
```
nums:    [1,  2,  3, 4]
postfix: [24, 24, 12, 4]
```

### Combining
```
index 0: postfix[1] = 24
index 1: prefix[0] * postfix[2] = 1 * 12 = 12
index 2: prefix[1] * postfix[3] = 2 * 4 = 8
index 3: prefix[2] = 6
```

## Pattern Recognition

This problem demonstrates:
- Prefix/suffix precomputation pattern
- Space optimization technique
- Avoiding division constraint workaround

## Related Problems

- Trapping Rain Water (similar prefix/suffix pattern)
- Maximum Product Subarray
- Subarray Product Less Than K

## Edge Cases

- Array with zeros
- Array with negative numbers
- Minimum length array (length 2)
- All elements are 1
- Very large products (within 32-bit limit)

## Files

- `solution.py`: Prefix/Postfix and Space Optimized implementations

