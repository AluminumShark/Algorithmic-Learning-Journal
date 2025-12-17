from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count how many students prefer each sandwich type: 0 or 1
        cnt = Counter(students)

        # Iterate through sandwiches in order
        for s in sandwiches:
            if cnt[s] > 0:
                # If at least one student wants this sandwich, serve it
                cnt[s] -= 1
            else:
                # If no one wants this sandwich, all remaining students get stuck
                break

        # Remaining students = leftover 0's + leftover 1's
        return cnt[0] + cnt[1]
