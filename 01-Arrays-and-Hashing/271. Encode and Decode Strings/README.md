# LeetCode 271: Encode and Decode Strings

## Overview

Design an algorithm to encode a list of strings to a single string and decode it back, handling any possible characters including delimiters.

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over a network and is decoded back to the original list of strings.

Implement the `encode` and `decode` methods.

**Example:**
```
Input: ["hello", "world"]
Encoded: "5#hello5#world"
Decoded: ["hello", "world"]

Input: ["we", "say", ":", "yes"]
Encoded: "2#we3#say1#:3#yes"
Decoded: ["we", "say", ":", "yes"]
```

## Algorithm

**Length Prefix Encoding**: Use length of each string followed by a delimiter.

**Key Steps (Encode):**
1. For each string, prepend its length
2. Add '#' as delimiter between length and content
3. Concatenate all encoded parts

**Key Steps (Decode):**
1. Find '#' to extract length prefix
2. Read exactly `length` characters after '#'
3. Move pointer to next encoded string
4. Repeat until end of string

## Complexity Analysis

- **Time Complexity:** O(n) for both encode and decode - n is total characters
- **Space Complexity:** O(n) - storing the encoded/decoded result

## Key Concepts

- **Length Prefix Protocol**: Common in network protocols
- **Delimiter Design**: '#' separates length from content
- **Unambiguous Encoding**: Length ensures correct parsing

## Implementation Details

### Why Length Prefix?
- Handles any character in strings (including '#')
- No escape sequences needed
- Efficient single-pass decoding

### Encoding Format
```
"hello" -> "5#hello"
"a#b"   -> "3#a#b"  (handles '#' in content)
""      -> "0#"     (handles empty strings)
```

### Two Pointer Decoding
- `L`: Start of length prefix
- `R`: Scans to find '#'
- Extract length, then exact substring

## Pattern Recognition

This problem demonstrates:
- Protocol design for serialization
- Length-prefixed encoding pattern
- Handling edge cases in string processing

## Alternative Approaches

### Escape Character
- Use escape sequences like '\#' for '#' in content
- More complex to implement
- Slower due to escape processing

### Non-ASCII Delimiter
- Use a character unlikely in input
- Not robust for arbitrary strings

## Related Problems

- Serialize and Deserialize Binary Tree
- Serialize and Deserialize BST
- Design HashMap

## Edge Cases

- Empty list of strings
- List containing empty strings
- Strings containing '#' character
- Strings containing digits
- Very long strings
- Unicode characters

## Files

- `solution.py`: Length prefix encode/decode implementation

