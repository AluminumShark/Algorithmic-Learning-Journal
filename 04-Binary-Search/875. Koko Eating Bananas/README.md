# LeetCode 875: Koko Eating Bananas

## Overview

Find the minimum eating speed for Koko to finish all bananas within given hours using binary search on the answer space.

## Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

**Example:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Algorithm

### Solution 1: Brute Force

**Key Steps:**
1. Try each possible eating speed from 1 to max(piles)
2. For each speed `k`, calculate total hours needed
3. Return the first speed where total hours ≤ h
4. Hours calculation: `(p + k - 1) // k` (ceiling division)

### Solution 2: Binary Search on Answer

**Key Steps:**
1. Binary search on the answer space [1, max(piles)]
2. For each candidate speed `k`, calculate total hours needed
3. If hours > h: speed too slow, search right half (`L = k + 1`)
4. If hours ≤ h: valid speed, try smaller (`R = k - 1`), track minimum valid speed
5. Return the minimum valid speed found

## Complexity Analysis

### Solution 1: Brute Force
- **Time Complexity:** O(max(p) * len(p)) - tries all speeds up to max pile
- **Space Complexity:** O(1) - only uses constant extra space

### Solution 2: Binary Search on Answer
- **Time Complexity:** O(len(p) * log(max(p))) - binary search with O(len(p)) validation
- **Space Complexity:** O(1) - only uses constant extra space

## Key Concepts

- **Binary Search on Answer**: Search the solution space instead of the input array
  - Answer space: [1, max(piles)]
  - Validation function: Check if a given speed can finish in h hours
  - Monotonic property: If speed k works, all speeds > k also work
- **Ceiling Division**: `(p + k - 1) // k` calculates ⌈p/k⌉ efficiently
- **Monotonic Function**: Hours needed decreases as speed increases

## Implementation Details

### Brute Force Approach
- Linear search through all possible speeds
- Simple but inefficient for large pile sizes
- No optimization needed

### Binary Search Approach
- Search space: [1, max(piles)]
- Validation: For each candidate k, sum up hours needed for all piles
- When hours ≤ h: valid answer, try smaller (R = k - 1)
- When hours > h: too slow, need faster (L = k + 1)
- Track minimum valid speed in `ans` variable

## Pattern Recognition

This problem demonstrates:
- Binary search on answer space (not on input array)
- Optimization problems with monotonic properties
- Validation function pattern
- Finding minimum/maximum valid value

## Use Cases

- Optimization problems with monotonic properties
- Finding minimum/maximum valid parameter
- Problems where direct calculation is expensive but validation is feasible
- Resource allocation problems

## Related Problems

- Capacity To Ship Packages Within D Days (LeetCode 1011)
- Split Array Largest Sum (LeetCode 410)
- Minimize Maximum Distance to Gas Station
- Binary search on answer variations

## Edge Cases

- Single pile with large value
- All piles have same size
- h equals number of piles (must eat one pile per hour)
- Very large pile values

## Files

- `solution.py`: Brute Force and Binary Search on Answer implementations

