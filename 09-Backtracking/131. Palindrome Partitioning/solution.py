# Time: O(N * 2^N)
# Space: O(N)
# Concept: The "Cut" Strategy. The loop 'j' decides where the current substring ends.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur, res = [], []
        
        def is_pal(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            # j defines the end of the current substring (the cut point)
            for j in range(i, len(s)):
                if is_pal(i, j):
                    cur.append(s[i : j + 1])
                    dfs(j + 1)
                    cur.pop()
        
        dfs(0)
        return res
