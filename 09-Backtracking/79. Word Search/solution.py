# Time: O(R * C * 4^L) (L is length of word)
# Space: O(L)
# Concept: Grid DFS + Backtracking (Marking visited cells and restoring them).


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r > R - 1 or c > C - 1 or board[r][c] == '#' or board[r][c] != word[i]):
                return False

            ch = board[r][c]
            board[r][c] = '#' # Mark visited

            res = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )

            board[r][c] = ch # Restore (Backtrack)

            return res
            
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False
