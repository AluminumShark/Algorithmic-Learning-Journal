from typing import List

# Solution 1: Brute Force-ish (Still O(n) average but can be O(n²) worst)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashSet = set(nums)
        for n in hashSet:
            curr = n
            count = 0
            while True:
                if curr in hashSet:
                    count += 1
                else:
                    break
                curr += 1
            ans = max(ans, count)
        return ans


# Solution 2: Optimized Set (O(n))
class SolutionOptimized:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashSet = set(nums)
        ans = 0
        
        for n in hashSet:
            # Only start counting from sequence beginning
            # A number is a sequence start if (n-1) is not in set
            if n - 1 not in hashSet:
                curr = n
                count = 1
                while curr + 1 in hashSet:
                    curr += 1
                    count += 1
                ans = max(ans, count)
        
        return ans

