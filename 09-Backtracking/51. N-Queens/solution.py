# Time: O(N!)
# Space: O(N^2) (Board storage)
# Concept: Backtracking with Set Constraints (Cols, Diag1 (r-c), Diag2 (r+c)).

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set() # (r - c)
        diag2 = set() # (r + c)
        board = [['.'] * n for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                dfs(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return res
