class Solution:
    """
    Check whether the input string has valid parentheses/brackets/braces.
    Use a stack to ensure correct matching and ordering.
    """

    def isValid(self, s: str) -> bool:
        # Odd-length strings can never be valid
        if len(s) % 2 == 1:
            return False
        
        stack = []

        for char in s:
            # Push opening brackets to stack
            if char in "([{":
                stack.append(char)

            # Handle closing brackets
            elif char == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif char == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            elif char == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        # Stack must be empty if all brackets matched
        return len(stack) == 0
