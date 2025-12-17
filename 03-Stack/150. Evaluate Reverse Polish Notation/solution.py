from typing import List

class Solution:
    """
    Evaluate Reverse Polish Notation (Postfix Expression)
    Use a stack to evaluate the expression.
    """
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        
        for t in tokens:
            if t not in ops:
                # Token is a number
                stack.append(int(t))
            else:
                # Token is an operator
                y = stack.pop()  # Second operand (top of stack)
                x = stack.pop()  # First operand
                
                if t == '+':
                    stack.append(x + y)
                elif t == '-':
                    stack.append(x - y)
                elif t == '*':
                    stack.append(x * y)
                else:  # Division
                    # Use int(x / y) for truncation toward zero
                    stack.append(int(x / y))
        
        return stack[-1]

