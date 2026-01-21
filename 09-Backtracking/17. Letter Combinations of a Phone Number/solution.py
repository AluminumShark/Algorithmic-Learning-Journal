# Time: O(4^N)
# Space: O(N)
# Concept: Mapping + Backtracking.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        cur, res = [], []
        mp = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def dfs(i):
            if i == len(digits):
                res.append(''.join(cur))
                return
            
            chs = mp[digits[i]]

            for j in range(len(chs)):
                cur.append(chs[j])
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res
