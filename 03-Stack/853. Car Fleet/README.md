# LeetCode 853: Car Fleet

## Overview

Determine how many car fleets will arrive at the destination, where faster cars behind slower cars form a single fleet.

## Problem Description

There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.

Each car `i` has a constant `speed[i]` (miles per hour) and initial `position[i]` (miles from start).

A car can never pass another car, but it can catch up and drive bumper to bumper at the same speed. The distance between them is ignored.

A **car fleet** is some non-empty set of cars driving at the same position and same speed.

Return the number of car fleets that will arrive at the destination.

**Example:**
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: 
- Cars starting at 10 and 8 become a fleet, meeting at 12
- Car at 5 and 3 become a fleet, meeting at 6
- Car at 0 never catches up
```

## Algorithm

**Stack + Sorting Approach**:

**Key Steps:**
1. Pair positions with speeds and sort by position (descending)
2. For each car (starting from closest to target):
   - Calculate time to reach target: `t = (target - position) / speed`
   - If time ≤ previous car's time: they form a fleet (skip)
   - Otherwise: new fleet starts
3. Return stack size (number of fleets)

## Complexity Analysis

- **Time Complexity:** O(n log n) - sorting dominates
- **Space Complexity:** O(n) - storing cars and stack

## Key Concepts

- **Fleet Formation**: Faster cars behind slower cars merge
- **Sorting by Position**: Process cars closest to target first
- **Time-Based Comparison**: Compare arrival times, not speeds

## Implementation Details

### Why Sort by Position Descending?
Cars closer to target determine if cars behind can catch up:
```
target = 10
Car A at position 8, speed 2 -> time = 1
Car B at position 5, speed 10 -> time = 0.5

But B cannot pass A, so B joins A's fleet (time = 1)
```

### Fleet Formation Logic
```python
if stack and t <= stack[-1]:
    continue  # Joins previous fleet
stack.append(t)  # New fleet
```

## Pattern Recognition

This problem demonstrates:
- Sorting for order processing
- Stack for tracking fleets
- Physics-based problem abstraction

## Visualization

```
Position: 0   3   5   8   10  |12 (target)
Speed:    1   3   1   4   2   |
Time:     12  3   7   1   1   |

Processing right to left:
- Car at 10: time=1, new fleet
- Car at 8: time=1, joins fleet (1 ≤ 1)
- Car at 5: time=7, new fleet (7 > 1)
- Car at 3: time=3, joins fleet (3 ≤ 7)
- Car at 0: time=12, new fleet (12 > 7)

Result: 3 fleets
```

## Related Problems

- Intersection of Two Arrays
- Merge Intervals
- Meeting Rooms II

## Edge Cases

- Single car
- All cars same position
- All cars same speed
- Cars that never catch up
- Cars all arriving at same time

## Files

- `solution.py`: Sorting and stack-based implementation

