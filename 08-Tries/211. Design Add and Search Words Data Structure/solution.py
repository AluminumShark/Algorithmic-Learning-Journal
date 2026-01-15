# Time: O(L) for add, O(26^k * L) for search (k = number of dots)
# Space: O(L)
# Concept: Trie + DFS Backtracking for '.' wildcard.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end
            
            ch = word[i]

            if ch == '.':
                return any(dfs(i + 1, child) for child in node.children.values())
            
            if ch not in node.children:
                return False
            
            return dfs(i + 1, node.children[ch])
        
        return dfs(0, self.root)
