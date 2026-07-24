class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"

        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == "+":
                    res = a + b
                elif tokens[i] == "-":
                    res = a - b
                elif tokens[i] == "*":
                    res = a * b
                else:
                    res = int(a / b)
                
                stack.append(res)
                
            else: 
                stack.append(tokens[i])
        
        return int(stack[0])