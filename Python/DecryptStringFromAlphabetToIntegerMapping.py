class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        res = ""
        s = list(s)
        
        while(s): 
            
            num = s.pop()
            
            if num == "#":
                num = s.pop()
                num = s.pop() + num 
            
            char = chr(ord('`') + int(num))
            res = char + res
        
        return res
