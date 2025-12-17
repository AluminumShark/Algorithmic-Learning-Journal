from typing import List
from collections import defaultdict

# Solution 1: Sorting (O(m * nlogn))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            key = sorted(s)
            key = ''.join(key)
            if key in mapping:
                mapping[key].append(s)
            else:
                mapping[key] = [s]
        return list(mapping.values())


# Solution 2: Char Count (O(m * n))
class SolutionCharCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            mapping[key].append(s)
        return list(mapping.values())

