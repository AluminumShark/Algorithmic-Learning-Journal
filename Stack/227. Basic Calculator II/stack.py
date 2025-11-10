class Solution:
    def calculate(self, s: str) -> int:
        size = len(s)
        stack = []          # Stack to hold intermediate results
        op = '+'            # Current operation; defaults to '+'
        index = 0

        while index < size:
            if s[index] == ' ':
                # Skip whitespace characters
                index += 1
                continue
            
            if s[index] in '0123456789':
                # Parse number manually using ASCII subtraction (ord)
                num = ord(s[index]) - ord('0')

                # Handle multi-digit numbers
                while index + 1 < size and s[index+1] in '0123456789':
                    index += 1
                    num = num * 10 + ord(s[index]) - ord('0')
                
                # Apply previous operation before updating op
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    # Use int() to truncate toward zero
                    top = stack.pop()
                    stack.append(int(top / num))
            
            elif s[index] in '+-*/':
                # Update the current operator
                op = s[index]
            
            index += 1
        
        # Final result is the sum of stack values
        return sum(stack)
