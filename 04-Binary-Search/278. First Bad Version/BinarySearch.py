# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    """
    Find the first bad version using Binary Search.
    Each call to isBadVersion(mid) tells us whether the bad version
    is at or before mid, or after mid.
    """

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        # Continue searching while the range is valid
        while left < right:
            mid = left + (right - left) // 2  # avoid potential overflow (good habit)
            
            # If mid is bad, the first bad version is at mid or before
            if isBadVersion(mid):
                right = mid
            else:
                # Otherwise, it's after mid
                left = mid + 1

        # At the end, left == right == first bad version
        return right
