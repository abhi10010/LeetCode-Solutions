class Solution:
    def maximum69Number (self, num: int) -> int:
        
        flag = 1
        n = str(num)
        
        for i in range(len(n)):
            
            if n[i] == '6' and flag == 1:
                flag = 0
                n = n[:i] + '9' + n[i+1:]
                
                return n
        
        return n
        
                
