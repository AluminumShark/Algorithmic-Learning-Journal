from typing import List

# Solution 1: Floyd's Cycle Detection (Tortoise and Hare)
# Time: O(n)
# Space: O(1)
# Concept: Treat the array as a Linked List where index i points to nums[i].
#          Use cycle detection to find the duplicate.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point
        S, F = nums[0], nums[0]
        while True:
            S = nums[S]          # Move slow pointer one step
            F = nums[nums[F]]    # Move fast pointer two steps
            if S == F:
                break
        
        # Phase 2: Find entrance to cycle (the duplicate)
        ptr1 = nums[0]
        ptr2 = S
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1


# Solution 2: Hash Set
# Time: O(n)
# Space: O(n)
class SolutionSet:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = set()
        for n in nums:
            if n not in mp:
                mp.add(n)
            else:
                return n

