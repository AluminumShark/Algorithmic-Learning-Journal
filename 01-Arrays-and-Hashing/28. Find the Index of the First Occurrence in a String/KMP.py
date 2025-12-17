class Solution:
    def generateNext(self, p):
        m = len(p)
        next = [0 for _ in range(m)]   # Prefix function (LPS array)
        left = 0                       # Length of current matched prefix
        
        # Build the prefix table
        for right in range(1, m):
            # If mismatch, shorten the prefix length using previous LPS value
            while left > 0 and p[left] != p[right]:
                left = next[left - 1]
            
            # If characters match, extend the prefix length
            if p[left] == p[right]:
                left += 1
            
            # Record the length of longest prefix-suffix for this position
            next[right] = left
        
        return next
    
    def kmp(self, T, p):
        n, m = len(T), len(p)
        if m == 0:
            return 0  # Empty pattern matches at index 0

        next = self.generateNext(p)    # Build the LPS (Longest Prefix Suffix) array
        j = 0                          # Pointer in pattern p
        
        # Scan through text T
        for i in range(n):
            # On mismatch, fall back in the pattern based on LPS table
            while j > 0 and T[i] != p[j]:
                j = next[j - 1]
            
            # If characters match, move both pointers
            if T[i] == p[j]:
                j += 1
            
            # Found a full match
            if j == m:
                return i - j + 1
        
        # No match found
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return self.kmp(haystack, needle)
