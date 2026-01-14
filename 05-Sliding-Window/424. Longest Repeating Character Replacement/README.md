# LeetCode 424: Longest Repeating Character Replacement

## Overview

Find the longest substring with the same letter after replacing at most `k` characters using a sliding window with frequency tracking.

## Problem Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' -> "AABBBBA"
```

## Algorithm

**Sliding Window with Frequency Tracking**: Maintain a window where the number of characters to replace (window size - max frequency) is at most `k`.

**Key Steps:**
1. Initialize frequency array `cnt[26]`, `L = 0`, `maxFreq = 0`
2. For each character at position `R`:
   - Increment frequency of current character
   - Update `maxFreq` (maximum frequency in current window)
   - While window is invalid (`(R - L + 1) - maxFreq > k`):
     - Decrement frequency of character at `L`
     - Move `L` forward
   - Update maximum length
3. Return maximum length found

## Complexity Analysis

- **Time Complexity:** O(n) - single pass, each character processed at most twice
- **Space Complexity:** O(1) - fixed-size frequency array of 26 elements

## Key Concepts

### Window Validity Condition

A window is valid if we can make all characters the same with at most `k` replacements:

```
Window size - Max frequency char count ≤ k
(R - L + 1) - maxFreq ≤ k
```

**Example:**
```
Window: "AABAB" (size = 5)
Frequencies: A=3, B=2
maxFreq = 3 (A appears most)
Characters to replace = 5 - 3 = 2

If k = 2: Valid (replace 2 B's with A's -> "AAAAA")
If k = 1: Invalid (need 2 replacements but only have 1)
```

### Why Track maxFreq?

- The optimal strategy is to keep the most frequent character and replace all others
- `maxFreq` represents the character we should keep
- `window_size - maxFreq` = minimum replacements needed

### Shrinking the Window

When `(R - L + 1) - maxFreq > k`:
- Window requires more than `k` replacements
- Shrink from left by moving `L` forward
- Decrement frequency of character leaving the window

**Note:** We don't need to update `maxFreq` when shrinking because:
- If the max frequency character leaves, the new `maxFreq` might be smaller
- But this only makes the window more restrictive (still valid if it was valid)
- The algorithm still works correctly, just might not shrink optimally

## Implementation Details

- `cnt = [0] * 26`: Fixed-size array for uppercase letters
- `ord(ch) - ord('A')`: Convert character to index (0-25)
- `maxFreq` only increases, never decreases (optimization)
- Window shrinks until constraint is satisfied

## Pattern Recognition

This problem demonstrates:
- Variable-size sliding window
- Frequency tracking in window
- Window validity constraint
- Shrink-until-valid pattern

## Use Cases

- Substring with constraint problems
- Character frequency analysis
- Window-based string transformations

## Related Problems

- Longest Substring Without Repeating Characters (LeetCode 3)
- Max Consecutive Ones III (LeetCode 1004)
- Minimum Window Substring (LeetCode 76)
- Sliding window variations

## Edge Cases

- Empty string
- k >= string length (return string length)
- All same characters
- k = 0 (find longest run of same character)

## Files

- `solution.py`: Sliding window with frequency tracking

