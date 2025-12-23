# LeetCode 3: Longest Substring Without Repeating Characters

## Overview

Find the length of the longest substring without repeating characters using a sliding window technique with a hash set.

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

**Example:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## Algorithm

**Variable-Size Sliding Window with Set**: Use two pointers to maintain a window with unique characters, tracked by a hash set.

**Key Steps:**
1. Initialize `L = 0`, `seen = set()`, `length = 0`
2. Iterate through string with `R` pointer:
   - While current character `ch` is in `seen`:
     - Remove `s[L]` from `seen`
     - Move `L` pointer forward
   - Add `ch` to `seen`
   - Update maximum length: `max(length, R - L + 1)`
3. Return `length`

## Complexity Analysis

- **Time Complexity:** O(n) - each character is visited at most twice (once by `R`, once by `L`)
- **Space Complexity:** O(n) or O(1) depending on charset
  - O(min(n, m)) where m is character set size
  - O(1) if limited to ASCII (128) or extended ASCII (256)

## Key Concepts

### Sliding Window with Set

- **Set for Uniqueness**: Use a set instead of dictionary for cleaner O(1) membership check
- **Shrink Until Valid**: When duplicate found, shrink window from left until duplicate is removed
- **Expand Always**: Right pointer always moves forward

### Window Invariant

The window `[L, R]` always contains unique characters:
```
s = "abcabcbb"
     L R        seen = {a, b, c}, length = 3
       L R      After encountering 'a': shrink until 'a' is removed
```

## Implementation Details

- Uses `set()` for O(1) add/remove/lookup
- `enumerate(s)` provides both index and character
- Window shrinks with `while` loop until constraint satisfied
- Length updated after each valid window expansion

## Pattern Recognition

This problem demonstrates:
- Variable-size sliding window technique
- Set-based uniqueness tracking
- Shrink-until-valid pattern
- Two-pointer window management

## Use Cases

- Longest unique sequence finding
- Substring analysis problems
- Window-based string processing
- Character uniqueness constraints

## Related Problems

- Longest Substring with At Most K Distinct Characters
- Minimum Window Substring (LeetCode 76)
- Longest Repeating Character Replacement (LeetCode 424)
- Permutation in String (LeetCode 567)

## Files

- `solution.py`: Sliding window with hash set implementation
