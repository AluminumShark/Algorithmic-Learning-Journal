class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        len1, len2 = len(haystack), len(needle)

        # Iterate through both strings
        while i < len1 and j < len2:
            if haystack[i] == needle[j]:
                # Characters match → move both pointers forward
                i += 1
                j += 1
            else:
                # Mismatch → reset j to 0 and shift i back
                # Move i to the next starting position after the first mismatch
                i = i - (j - 1)
                j = 0

        # If all characters in needle matched, return the start index
        if j == len2:
            return i - j
        else:
            return -1
