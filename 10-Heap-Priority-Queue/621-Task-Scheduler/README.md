# 621. Task Scheduler

## Problem Description

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

**Example 1:**
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

**Example 2:**
```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

**Example 3:**
```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

## Solutions

### Solution 1: Math / Formula (Optimal)

**Key Insight:** The minimum time is determined by the most frequent task(s).

**Formula:**
```
minTime = (maxFreq - 1) * (n + 1) + numMax
result = max(len(tasks), minTime)
```

**Explanation:**
1. Find the task with maximum frequency (`maxFreq`)
2. Count how many tasks have this maximum frequency (`numMax`)
3. Calculate the minimum slots needed:
   - We need `maxFreq - 1` "chunks" of tasks with idle slots
   - Each chunk has size `n + 1` (one slot for the max-freq task + n cooldown slots)
   - Add `numMax` for the last occurrence of all max-frequency tasks
4. The result is the maximum of:
   - Total number of tasks (if no idle time is needed)
   - Calculated minimum time (if idle time is required)

**Visual Example:**
```
tasks = ["A","A","A","B","B","B"], n = 2
maxFreq = 3, numMax = 2 (both A and B appear 3 times)

Chunks: (maxFreq - 1) = 2 chunks
Each chunk size: (n + 1) = 3
minTime = 2 * 3 + 2 = 8

Layout: A B _ | A B _ | A B
        └─chunk 1─┘ └─chunk 2─┘ └final┘
```

**Complexity:**
- **Time:** O(N) - single pass to count frequencies
- **Space:** O(1) - fixed array of size 26

**Optimization Note:** The line counting `numMax` can be replaced with `freq.count(maxFreq)` for cleaner code.

---

### Solution 2: Greedy

**Approach:** Calculate idle slots and fill them greedily.

**Algorithm:**
1. Count frequency of each task
2. Sort frequencies
3. Calculate initial idle slots: `(maxFreq - 1) * n`
4. Fill idle slots with other tasks (up to `maxFreq - 1` of each)
5. Return `max(0, idle) + len(tasks)`

**Why it works:**
- Start with the maximum possible idle time
- Greedily reduce idle slots by scheduling other tasks
- If idle becomes negative, it means we have enough tasks to fill all slots

**Complexity:**
- **Time:** O(N log N) - dominated by sorting
- **Space:** O(1) - fixed array of size 26

---

### Solution 3: Heap Simulation

**Approach:** Simulate the actual task scheduling process using a heap and queue.

**Data Structures:**
- **Max-Heap (`h`)**: Stores available tasks by their remaining count (as negative values)
- **Queue (`q`)**: Stores tasks in cooldown as `[remaining_count, available_time]`

**Algorithm:**
1. Build a max-heap with all task frequencies (negated for max-heap behavior)
2. For each time unit:
   - If heap is empty, fast-forward time to when the next task becomes available
   - Otherwise, pop the most frequent task and execute it
   - If the task still has remaining instances, add it to the cooldown queue
   - Check if any task in the queue is ready to be added back to the heap
3. Continue until both heap and queue are empty

**Complexity:**
- **Time:** O(N log 26) = O(N) - at most 26 different tasks
- **Space:** O(1) - heap and queue store at most 26 tasks

---

## Key Concepts

### 1. Math vs Simulation Trade-off

- **Math approach**: O(N) but requires mathematical insight
- **Simulation approach**: More intuitive but slightly slower due to heap operations

### 2. Idle Time Calculation

The core problem is determining how much idle time is needed. This depends on:
- The frequency of the most common task
- The cooldown period `n`
- The distribution of other tasks

### 3. Why Max-Heap in Simulation?

We always want to schedule the most frequent remaining task to minimize future idle time. This greedy choice leads to the optimal solution.

### 4. When is Result > len(tasks)?

When there aren't enough different tasks to fill the cooldown periods between the most frequent task.

Example: `tasks = ["A","A","A","B"], n = 2`
- Need: A _ _ A _ _ A (at least 8 slots)
- Have: 4 tasks
- Result: 8 (requires 4 idle slots)

### 5. When is Result = len(tasks)?

When tasks are diverse enough that we can always find a different task to schedule during cooldown periods.

Example: `tasks = ["A","B","C","D","E","F"], n = 2`
- Have enough different tasks to avoid any idle time
- Result: 6

## Comparison

| Approach | Time | Space | Complexity | When to Use |
|----------|------|-------|------------|-------------|
| Math | O(N) | O(1) | Low (if you know the formula) | Interviews, optimal solution |
| Greedy | O(N log N) | O(1) | Medium | Easier to derive on the spot |
| Heap | O(N) | O(1) | Medium-High | When simulation is more intuitive |

## Recommendation

For **interviews**: Learn the **Math approach** - it's the fastest and most impressive once you understand the formula.

For **understanding**: Study the **Heap simulation** - it makes the problem concrete and helps build intuition.
