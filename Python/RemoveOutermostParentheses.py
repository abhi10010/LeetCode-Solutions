class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        p, l = 0, []
        
        for i in S:
            
            if i == ')':
                p -= 1
            
            if p > 0:
                l.append(i)
            
            if i == '(':
                p += 1
        
        return ''.join(l) 
            
