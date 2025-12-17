# LeetCode 739: Daily Temperatures

## Overview

Find the number of days until a warmer temperature for each day using a monotonic stack approach.

## Problem Description

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Algorithm

**Monotonic Decreasing Stack**: Use a stack to store indices of temperatures waiting for a warmer day.

**Key Steps:**
1. Initialize an empty stack and result array filled with zeros
2. Iterate through temperatures with index `i`:
   - While stack is non-empty and `temperatures[i] > temperatures[stack[-1]]`:
     - Current temperature is warmer for the day at stack top
     - Calculate days: `answer[stack_top] = i - stack_top`
     - Pop from stack
   - Push current index `i` to stack
3. Return answer array (days with no warmer temperature remain 0)

## Complexity Analysis

- **Time Complexity:** O(n) - each index is pushed and popped at most once
- **Space Complexity:** O(n) - for the stack in worst case

## Key Insight

The monotonic decreasing stack stores indices of temperatures in decreasing order:
- When a warmer temperature appears, it resolves all cooler temperatures in the stack
- The difference between indices gives the number of days to wait
- Elements remaining in stack have no warmer future day (answer remains 0)

## Implementation Details

### Stack Stores Indices
- Store indices instead of values for distance calculation
- Allows direct calculation: `i - index`
- More efficient than storing pairs

### Monotonic Property
- Stack maintains decreasing temperature order
- Top element is the coolest among unresolved days
- Warmer temperature resolves multiple days at once

### Result Initialization
- Initialize with zeros (handles days with no warmer temperature)
- Only update when warmer temperature is found

## Pattern Recognition

This problem demonstrates:
- Monotonic stack pattern
- Next greater element variant (with distance)
- Index-based stack operations
- One-pass solution with stack

## Use Cases

- Stock price analysis (days until higher price)
- Weather forecasting applications
- Time-series data analysis
- Next greater element with distance

## Related Problems

- Next Greater Element I
- Next Greater Element II
- Trapping Rain Water
- Largest Rectangle in Histogram

## Edge Cases

- All temperatures in decreasing order (all zeros)
- All temperatures in increasing order (all ones)
- Single temperature
- No warmer future day (remains 0)

## Alternative Approaches

1. **Brute Force**: O(n²)
   - For each day, search forward for warmer day
   - Inefficient for large inputs

2. **Dynamic Programming**: O(n)
   - More complex implementation
   - Similar time complexity but less intuitive

## Files

- `MonotoneStack.py`: Monotonic stack implementation with index tracking

