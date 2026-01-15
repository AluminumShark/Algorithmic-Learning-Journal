# Time: O(row * col * 3^L)
# Space: O(S) (Trie size)
# Concept: Backtracking on Grid + Trie for fast lookup + Pruning (remove found words).


class TrieNode:
    __slots__ = ("children", "word")
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            cur = root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = w
        
        ans = []
        R, C = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            nxt = node.children[ch]

            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None # Avoid duplicates
            
            board[r][c] = '#' # Mark visited

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)
            if r < R - 1 and board[r + 1][c] != '#':
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)
            if c < C - 1 and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)
            
            board[r][c] = ch # Backtrack

            # Optimization: Leaf node pruning
            if not nxt.children:
                node.children.pop(ch, None)
            
        for r in range(R):
            for c in range(C):
                dfs(r, c, root)

        return ans
