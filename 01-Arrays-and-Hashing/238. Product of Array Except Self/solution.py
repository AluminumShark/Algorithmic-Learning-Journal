from typing import List

# Solution 1: Prefix & Postfix Arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Build prefix products
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        # Build postfix products
        postfix = [1] * n
        postfix[n - 1] = nums[n - 1]
        for j in range(n - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j]
        
        # Combine prefix and postfix
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(postfix[1])
            elif i == n - 1:
                ans.append(prefix[n - 2])
            else:
                ans.append(prefix[i - 1] * postfix[i + 1])
        return ans


# Solution 2: O(1) Space Optimization
class SolutionOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        # Build prefix products in ans array
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        
        # Multiply with postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans

