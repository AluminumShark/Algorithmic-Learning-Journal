# LeetCode 3: Longest Substring Without Repeating Characters

## Overview

Find the length of the longest substring without repeating characters using a sliding window technique.

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

**Example:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

## Algorithm

**Variable-Size Sliding Window**: Use two pointers to maintain a window with unique characters, expanding when possible and shrinking when duplicates are found.

**Key Steps:**
1. Initialize two pointers: `left = 0` and `right = 0`
2. Use a dictionary to track character frequencies in current window
3. Expand window by moving `right` pointer:
   - Add `s[right]` to window dictionary
4. Shrink window when duplicate found:
   - While `window[s[right]] > 1` (duplicate exists):
     - Remove `s[left]` from window
     - Move `left` pointer forward
5. Update maximum length: `max(result, right - left + 1)`
6. Continue until `right` reaches end of string

## Complexity Analysis

- **Time Complexity:** O(n) - each character is visited at most twice (once by `right`, once by `left`)
- **Space Complexity:** O(min(n, m)) - where n is string length and m is character set size (dictionary storage)

## Key Insight

The sliding window maintains the invariant that all characters in `[left, right]` are unique. When a duplicate is detected, we shrink from the left until the duplicate is removed.

## Alternative Approaches

1. **Hash Set with Character Index Mapping**: O(n) time
   - Store last occurrence index of each character
   - When duplicate found, jump `left` directly to `last_index + 1`
   - Slightly more efficient but similar complexity

2. **Brute Force**: O(n³) time
   - Check all possible substrings
   - Not efficient for large inputs

## Implementation Details

- Dictionary-based frequency tracking
- Expand-while-valid, shrink-until-valid pattern
- Window size tracked by `right - left + 1`
- Maximum length updated at each valid window state

## Pattern Recognition

This problem demonstrates:
- Variable-size sliding window technique
- Two-pointer technique
- Character frequency tracking
- Window maintenance with constraints

## Use Cases

- Longest unique sequence finding
- Substring analysis problems
- Window-based string processing
- Pattern matching variations

## Related Problems

- Longest Substring with At Most K Distinct Characters
- Minimum Window Substring
- Longest Substring with At Most Two Distinct Characters
- Substring with Concatenation of All Words

## Optimization Note

The current implementation uses a while loop to shrink the window. An optimized version can use a hash map storing the last occurrence index of each character:
- When duplicate found: `left = max(left, last_index[s[right]] + 1)`
- This avoids the shrinking loop and directly jumps to the correct position

## Files

- `SlidingWindow.py`: Variable-size sliding window with dictionary tracking

