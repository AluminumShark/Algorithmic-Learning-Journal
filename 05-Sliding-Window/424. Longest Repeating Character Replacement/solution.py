# Time: O(n)
# Space: O(1) (since map is max size 26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        L = 0
        length = 0
        maxFreq = 0
        for R, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            cnt[idx] += 1
            maxFreq = max(maxFreq, cnt[idx])
            
            # If current window size minus max freq char > k, we need to shrink window
            while (R - L + 1) - maxFreq > k:
                cnt[ord(s[L]) - ord('A')] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length

