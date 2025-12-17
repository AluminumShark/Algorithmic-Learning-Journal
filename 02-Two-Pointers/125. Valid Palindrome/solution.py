class Solution:
    """
    Valid Palindrome
    Check if a string is a palindrome using two pointers, 
    considering only alphanumeric characters and ignoring cases.
    """
    
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        
        while L < R:
            # Skip non-alphanumeric characters from left
            if not s[L].isalnum():
                L += 1
                continue
            
            # Skip non-alphanumeric characters from right
            if not s[R].isalnum():
                R -= 1
                continue
            
            # Compare characters (case-insensitive)
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True

