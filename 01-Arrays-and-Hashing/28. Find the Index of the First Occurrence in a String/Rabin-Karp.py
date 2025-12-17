class Solution:
    def rabinCarp(self, T, p):
        len1, len2 = len(T), len(p)
        hashP = hash(p)  # Compute hash of pattern p once
        
        # Slide a window of size len2 over T
        for i in range(len1 - len2 + 1):
            hashT = hash(T[i : i + len2])  # Compute hash of current substring
            
            # Only compare strings if hashes match (to avoid collisions)
            if hashP != hashT:
                continue

            # Collision check: verify character by character
            k = 0
            for j in range(len2):
                if T[i + j] == p[j]:
                    k += 1
                # If all characters matched, return the starting index
                if k == len2:
                    return i
                    
        # Pattern not found
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # Wrapper for LeetCode API
        return self.rabinCarp(haystack, needle)
