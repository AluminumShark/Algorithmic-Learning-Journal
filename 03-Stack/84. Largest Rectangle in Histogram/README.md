# LeetCode 84: Largest Rectangle in Histogram

## Overview

Find the largest rectangular area in a histogram using a monotonic stack approach.

## Problem Description

Given an array of integers `heights` representing the histogram's bar heights where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Example:**
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area = 10 (height 5, width 2)

     _
    | |
  _ | |
 | || |  _
 | || |_| |
_| || || ||_
2  1 5 6 2 3
```

## Algorithm

**Monotonic Stack Approach**:

**Key Steps:**
1. Append 0 to heights to force processing of remaining bars
2. Maintain a stack of indices in increasing order of heights
3. When a shorter bar is encountered:
   - Pop bars and calculate their max rectangle area
   - Width = current index - left boundary - 1
   - Update maximum area
4. Push current index to stack

## Complexity Analysis

- **Time Complexity:** O(n) - each element pushed and popped at most once
- **Space Complexity:** O(n) - stack storage

## Key Concepts

- **Monotonic Stack**: Maintains increasing order
- **Width Calculation**: Find left and right boundaries for each bar
- **Sentinel Value**: Append 0 to flush remaining bars

## Implementation Details

### Why Append 0?
Ensures all bars in stack are processed at the end:
```python
heights.append(0)  # Guarantees stack empties
```

### Width Calculation
When bar at index `pop_idx` is popped with current index `i`:
```
Left boundary: stack[-1] if stack else -1
Right boundary: i - 1
Width: (i - 1) - (left + 1) + 1 = i - left - 1
```

### Example Walkthrough
```
heights = [2, 1, 5, 6, 2, 3, 0]
                              ^ (appended)

i=0, h=2: stack=[0]
i=1, h=1: pop 0, area=2*1=2, stack=[1]
i=2, h=5: stack=[1,2]
i=3, h=6: stack=[1,2,3]
i=4, h=2: pop 3, area=6*1=6
          pop 2, area=5*2=10
          stack=[1,4]
i=5, h=3: stack=[1,4,5]
i=6, h=0: pop 5, area=3*1=3
          pop 4, area=2*4=8
          pop 1, area=1*6=6

Max = 10
```

## Pattern Recognition

This problem demonstrates:
- Monotonic stack pattern
- Finding next smaller element
- Rectangle area calculation

## Monotonic Stack Visualization

```
Stack maintains increasing heights:
Before: [1, 2, 5, 6]
After encountering 2: 
  - Pop 6 (area = 6 × 1)
  - Pop 5 (area = 5 × 2)
  - Stack: [1, 2, 2]
```

## Related Problems

- Maximal Rectangle (LeetCode 85)
- Trapping Rain Water (LeetCode 42)
- Daily Temperatures (LeetCode 739)

## Edge Cases

- Single bar
- All bars same height
- Increasing heights
- Decreasing heights
- Heights with zeros

## Files

- `solution.py`: Monotonic stack implementation

