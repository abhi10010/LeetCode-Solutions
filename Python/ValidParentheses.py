class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        stack = []
        p = 0
        
        for i in s:
            
            if i in ['(', '{', '[']:
                p += 1
                stack.append(i)
            
            elif stack and i == ')' and stack[-1] == '(':
                p += 1
                stack.pop()
                
            elif stack and i == '}' and stack[-1] == '{':
                p += 1
                stack.pop()
                
            elif stack and i == ']' and stack[-1] == '[':
                p += 1
                stack.pop()
                
        return not stack and p == len(s)
                
