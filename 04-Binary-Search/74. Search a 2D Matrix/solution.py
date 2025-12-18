from typing import List

# Solution 1: Brute Force
# Time: O(m * n)
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            if target > matrix[r][-1]:
                continue
            for c in range(m):
                if target > matrix[r][c]:
                    continue
                if matrix[r][c] == target:
                    return True
        return False


# Solution 2: Binary Search (Treat 2D as 1D)
# Time: O(log(m * n))
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        L, R = 0, (n * m - 1)
        while L <= R:
            mid = (L + R) // 2
            r, c = (mid // m), (mid % m)
            val = matrix[r][c]
            if val == target:
                return True
            else:
                if val < target:
                    L = mid + 1
                else:
                    R = mid - 1
        return False

