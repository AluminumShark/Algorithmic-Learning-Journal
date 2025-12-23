# Time: O(n)
# Space: O(n) or O(1) depending on charset
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        L = 0
        for R, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[L])
                L += 1
            seen.add(ch)
            length = max(length, R - L + 1)
        return length

