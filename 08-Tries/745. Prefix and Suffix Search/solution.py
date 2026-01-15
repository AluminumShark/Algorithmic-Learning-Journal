# Time: O(N * L^3) construction, O(1) search
# Space: O(N * L^3)
# Concept: Generate all Prefix + '#' + Suffix combinations and store in Hash Map.

class WordFilter:
    def __init__(self, words: List[str]):
        self.mp = {}
        for idx, w in enumerate(words):
            L = len(w)
            prefixes = [w[:i] for i in range(L + 1)]
            suffixes = [w[j:] for j in range(L + 1)]

            for p in prefixes:
                for s in suffixes:
                    self.mp[p + '#' + s] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.mp.get(pref + '#' + suff, -1)
