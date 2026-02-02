# Solution 1: Math / Geometry
# Time: O(N)
# Space: O(1)
# Concept: Calculate max idle slots based on the most frequent task.
# Formula: (maxFreq - 1) * (n + 1) + numMax
from typing import List

class SolutionMath:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        maxFreq = max(freq)
        # Optimization note: could use freq.count(maxFreq)
        numMax = 0
        for f in freq:
            if f == maxFreq:
                numMax += 1
        minLen = (maxFreq - 1) * (n + 1) + numMax
        return max(len(tasks), minLen)


# Solution 2: Greedy
# Time: O(N log N) for sorting
# Space: O(1)
class SolutionGreedy:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1

        cnt.sort()
        maxf = cnt[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(cnt[i], maxf - 1)

        return max(0, idle) + len(tasks)


# Solution 3: Heap Simulation
# Time: O(N * log 26) -> O(N)
# Space: O(1)
import heapq
from collections import Counter, deque

class SolutionHeap:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        h = [-cnt for cnt in counter.values()]
        heapq.heapify(h)
        q = deque()
        time = 0

        while h or q:
            time += 1
            if not h:
                time = q[0][1]

            else:
                cnt = 1 + heapq.heappop(h)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time
