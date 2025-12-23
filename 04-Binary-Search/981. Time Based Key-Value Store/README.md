# LeetCode 981: Time Based Key-Value Store

## Overview

Design a time-based key-value data structure that can store multiple values for the same key at different timestamps and retrieve the most recent value at or before a given timestamp.

## Problem Description

Design a time-based key-value data structure that can:

- Store multiple values for the same key at different time stamps
- Retrieve the key's value at a certain timestamp

Implement the `TimeMap` class:

- `TimeMap()`: Initializes the object
- `void set(String key, String value, int timestamp)`: Stores the key with value at the given timestamp
- `String get(String key, int timestamp)`: Returns a value such that `set` was called previously with `timestamp_prev <= timestamp`. If there are multiple such values, return the value with the largest `timestamp_prev`. If there are no values, return `""`

**Example:**
```
Input:
["TimeMap", "set", "get", "get", "set", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4]]

Output: [null, null, "bar", "bar", null, "bar2"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store "bar" at timestamp 1
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar" (largest timestamp <= 3)
timeMap.set("foo", "bar2", 4); // store "bar2" at timestamp 4
timeMap.get("foo", 4);         // return "bar2"
```

## Algorithm

**Binary Search on Sorted Timestamps**: Since timestamps are strictly increasing for each key, use binary search to find the largest timestamp ≤ query timestamp.

### set() Operation
1. If key doesn't exist, create empty list
2. Append `(timestamp, value)` tuple to key's list
3. Timestamps are guaranteed to be strictly increasing

### get() Operation
1. If key doesn't exist, return `""`
2. Binary search for largest timestamp ≤ query timestamp
3. Track best answer found during search
4. Return best answer (or `""` if none found)

## Complexity Analysis

### set() Operation
- **Time Complexity:** O(1) amortized - append to list
- **Space Complexity:** O(1) per call

### get() Operation
- **Time Complexity:** O(log n) - binary search on timestamp list
- **Space Complexity:** O(1) - only uses constant extra space

### Overall Space
- **Space Complexity:** O(n) - storing all key-value-timestamp tuples

## Key Concepts

### Binary Search for Floor Value

Finding the largest value ≤ target (floor):
```python
while L <= R:
    mid = (L + R) // 2
    if ts <= timestamp:
        ans = val      # Valid candidate, save it
        L = mid + 1    # Try to find larger valid timestamp
    else:
        R = mid - 1    # Timestamp too large, search left
```

### Timestamp Ordering Guarantee

The problem guarantees timestamps are strictly increasing for each key:
- `set("foo", "bar", 1)`
- `set("foo", "bar2", 4)`
- List for "foo": `[(1, "bar"), (4, "bar2")]` - already sorted!

## Implementation Details

- Use dictionary mapping key → list of (timestamp, value) tuples
- Tuples stored in insertion order (already sorted by timestamp)
- Binary search finds floor value efficiently
- Return empty string for missing keys or no valid timestamps

## Pattern Recognition

This problem demonstrates:
- Binary search for floor/ceiling values
- Design problems with multiple operations
- Time-series data storage patterns
- Efficient lookup in sorted data

## Use Cases

- Version control systems
- Cache with expiration
- Time-series databases
- Audit logging systems

## Related Problems

- Design HashMap (LeetCode 706)
- Design HashSet (LeetCode 705)
- Binary search variations
- Design problems

## Files

- `solution.py`: TimeMap implementation with binary search

