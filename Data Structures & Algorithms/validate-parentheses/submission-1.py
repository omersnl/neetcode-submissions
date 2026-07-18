class Solution:
    def isValid(self, s: str) -> bool:
        hashbracket = {"]" : "[", "}": "{", ")": "("}

        stack = []

        for b in s:
            if b in hashbracket:
                if stack and stack[-1] == hashbracket[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
            

        return True if not stack else False
                
