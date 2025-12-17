# LeetCode 1: Two Sum

## Overview

Find two numbers in an array that add up to a target value using hash map for efficient lookup.

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Input: nums = [3,2,4], target = 6
Output: [1,2]
```

## Algorithm

### Solution 1: Basic Hash Map (Two-Pass)

**Key Steps:**
1. First pass: Build a mapping of `(target - num)` → index
2. Second pass: Check if current number exists in the mapping
3. Ensure indices are different before returning

### Solution 2: Optimized One-Pass Hash Map

**Key Steps:**
1. Single pass through the array
2. For each number, check if complement `(target - num)` exists in map
3. If found, return current index and stored index
4. Otherwise, add current number and index to map

## Complexity Analysis

### Solution 1: Two-Pass Hash Map
- **Time Complexity:** O(n) - two passes through the array
- **Space Complexity:** O(n) - hash map stores all elements

### Solution 2: One-Pass Hash Map
- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hash map stores at most n elements

## Key Concepts

- **Hash Map**: O(1) average lookup for complement
- **Complement Pattern**: Store `target - num` to find pairs
- **One-Pass Optimization**: Build and query map simultaneously

## Implementation Details

### Two-Pass Approach
- Separates building and querying phases
- Must check `idx1 != idx2` to avoid using same element

### One-Pass Approach
- More elegant and efficient
- Previous elements are in map when checking current element
- Naturally avoids using same element twice

## Pattern Recognition

This problem demonstrates:
- Hash map for pair finding
- Complement search pattern
- Foundation for k-sum problems

## Related Problems

- Two Sum II (LeetCode 167) - Sorted array variant
- 3Sum (LeetCode 15)
- 4Sum (LeetCode 18)
- Two Sum III - Data Structure Design

## Edge Cases

- Two elements that equal target
- Negative numbers
- Duplicate values with valid answer
- Array with only two elements

## Files

- `solution.py`: Two-Pass and One-Pass Hash Map implementations

