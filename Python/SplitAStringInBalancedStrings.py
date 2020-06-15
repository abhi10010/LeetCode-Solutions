class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        l, r, res = 0, 0, 0
        
        for i in s:
            
            if i=='R':
                r += 1
            elif i=='L':
                l += 1
            
            if l == r:
                res += 1
                l = 0
                r = 0
        
        return res
