# LeetCode 150: Evaluate Reverse Polish Notation

## Overview

Evaluate an arithmetic expression in Reverse Polish Notation (postfix notation) using a stack.

## Problem Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note:** Division between two integers truncates toward zero.

**Example:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 4 + 2 = 6
```

## Algorithm

**Stack-Based Evaluation**:

**Key Steps:**
1. Iterate through each token
2. If token is a number, push to stack
3. If token is an operator:
   - Pop two operands (y first, then x)
   - Apply operator: `x op y`
   - Push result back to stack
4. Final result is the only element in stack

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through tokens
- **Space Complexity:** O(n) - stack stores operands

## Key Concepts

- **Postfix Notation**: Operator comes after operands
- **Stack**: Natural fit for postfix evaluation
- **Order Matters**: For `-` and `/`, operand order is important

## Implementation Details

### Operand Order
```
tokens: ["10", "3", "-"]
Stack after "10": [10]
Stack after "3": [10, 3]
Pop y = 3, pop x = 10
Result: x - y = 10 - 3 = 7
```

### Division Truncation
```python
# Python's // floors toward negative infinity
# Problem requires truncation toward zero
# Use int(x / y) instead of x // y

-7 // 2 = -4  # Wrong for this problem
int(-7 / 2) = -3  # Correct truncation toward zero
```

## Pattern Recognition

This problem demonstrates:
- Stack for expression evaluation
- Postfix notation processing
- Handling operator precedence implicitly

## Why Reverse Polish Notation?

1. No parentheses needed
2. No operator precedence rules to handle
3. Easy to evaluate with a stack
4. Used in calculators and compilers

## Related Problems

- Basic Calculator (LeetCode 224)
- Basic Calculator II (LeetCode 227)
- Parse Lisp Expression

## Edge Cases

- Single number
- Negative numbers
- Division resulting in truncation
- Nested operations
- Large numbers

## Files

- `solution.py`: Stack-based RPN evaluation

