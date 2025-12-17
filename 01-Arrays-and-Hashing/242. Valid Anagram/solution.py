from typing import List
from collections import Counter

# Solution 1: Hash Map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        return True


# Solution 2: Counter (One-liner)
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

