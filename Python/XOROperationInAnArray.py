class Solution:
    def xorOperation(self, n: int, start: int) -> int: 
        
        i,j = 0, start
        
        while i<n:
            
            if j == start:
                ans = j
            
            else:
                ans ^= j
            
            j += 2
            i += 1
        
        return ans
