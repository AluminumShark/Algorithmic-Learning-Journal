class Solution:
    """
    Longest Substring Without Repeating Characters
    Use a sliding window to maintain a substring with unique characters.
    Expand the window by moving `right`, and shrink it by moving `left`
    whenever a duplicate character is found.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0          # Two pointers defining the current window
        window = dict()             # Dictionary to count character frequencies
        result = 0                  # Length of the longest substring found

        while right < len(s):
            # Add the new character to the window
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            
            # If a character appears more than once, shrink from the left
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            # Update the maximum window size
            result = max(result, right - left + 1)
            right += 1
        
        return result
