class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []                 # Final answers for each element in nums1
        stack = []               # Monotonic decreasing stack storing candidates from nums2
        numsMap = dict()         # Map: value in nums2 -> its next greater element

        # Build next-greater mapping by scanning nums2 once
        for num in nums2:
            # While current num is greater than the stack's top,
            # current num is the "next greater" for that top element.
            while stack and num > stack[-1]:
                numsMap[stack[-1]] = num
                stack.pop()
            # Maintain a decreasing stack (top is smallest so far)
            stack.append(num)

        # Any values still in stack have no next greater; they map to -1 implicitly.
        # Answer each query in nums1 using the precomputed map.
        for num in nums1:
            ans.append(numsMap.get(num, -1))
        
        return ans
