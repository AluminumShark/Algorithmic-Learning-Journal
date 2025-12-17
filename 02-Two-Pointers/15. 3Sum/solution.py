from typing import List

# Solution 1: Brute Force with Set Conversion
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            L, R = 0, n - 1
            while L < i < R:
                curSum = nums[L] + nums[i] + nums[R]
                if curSum < 0:
                    L += 1
                elif curSum > 0:
                    R -= 1
                else:
                    ans.append([nums[L], nums[i], nums[R]])
                    L += 1
                    R -= 1
        
        # Remove duplicates using set of tuples
        return [list(t) for t in set(tuple(x) for x in ans)]


# Solution 2: Optimized Two Pointers (No Set)
class SolutionOptimized:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n):
            # Skip duplicate values for i
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            L, R = i + 1, n - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                    # Skip duplicates for L and R
                    while L < R and nums[L - 1] == nums[L]:
                        L += 1
                    while L < R and nums[R + 1] == nums[R]:
                        R -= 1
        
        return ans

