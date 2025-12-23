# LeetCode 121: Best Time to Buy and Sell Stock

## Overview

Find the maximum profit from a single buy-sell transaction by tracking the minimum price seen so far.

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done, max profit = 0.
```

## Algorithm

**One Pass with Minimum Tracking**: Track the lowest price seen so far and calculate potential profit at each step.

**Key Steps:**
1. Initialize `lowestBuy = infinity` and `best_profit = 0`
2. For each price in array:
   - Update `lowestBuy = min(lowestBuy, price)`
   - Calculate current profit: `price - lowestBuy`
   - Update `best_profit = max(best_profit, current_profit)`
3. Return `best_profit`

## Complexity Analysis

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(1) - only uses constant extra space

## Key Concepts

### Sliding Window Perspective

This problem can be viewed as a simplified sliding window:
- Left boundary: the day we buy (lowest price so far)
- Right boundary: the day we sell (current day)
- Window property: maximize `prices[R] - prices[L]`

```
prices = [7, 1, 5, 3, 6, 4]
              L        R
           buy=1    sell=6  → profit = 5
```

### Greedy Approach

At each position, we greedily:
1. Track the best buying opportunity (minimum price seen)
2. Calculate the best selling opportunity (current price - minimum)
3. Keep the overall maximum profit

### Why This Works

- We must buy before we sell
- By tracking the minimum price seen so far, we always have the best possible buying price available
- For each day, we check if selling today would give us a better profit

## Implementation Details

- `lowestBuy = float('inf')`: Initialize to infinity so any price becomes the new minimum
- `best_profit = 0`: If no profit possible, return 0 (not negative)
- Single pass: Calculate both min price and max profit simultaneously

## Pattern Recognition

This problem demonstrates:
- One-pass optimization
- Tracking minimum/maximum while iterating
- Implicit two-pointer (buy day, sell day)
- Greedy decision making

## Use Cases

- Stock trading optimization
- Buy low, sell high scenarios
- Finding maximum difference in sequence
- Optimization with ordering constraints

## Related Problems

- Best Time to Buy and Sell Stock II (LeetCode 122) - multiple transactions
- Best Time to Buy and Sell Stock III (LeetCode 123) - at most 2 transactions
- Best Time to Buy and Sell Stock IV (LeetCode 188) - at most k transactions
- Maximum Subarray (LeetCode 53) - similar pattern

## Edge Cases

- Prices always decreasing (return 0)
- Single element array (return 0)
- All same prices (return 0)
- Minimum at the end (return 0)

## Files

- `solution.py`: One-pass solution tracking minimum price

