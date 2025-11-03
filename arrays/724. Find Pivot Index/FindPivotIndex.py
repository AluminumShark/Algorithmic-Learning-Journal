class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = None
        right = None
        pivotIdx = None
        
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = sum(nums[i+1:])
            elif i == len(nums) - 1:
                left = sum(nums[:i])
                right = 0
            else:
                left = sum(nums[:i])
                right = sum(nums[i+1:])

            if left == right:
                pivotIdx = i
                break

        if pivotIdx != None:
            return pivotIdx
        else:
            return -1
