class Solution:
    def maxPower(self, s: str) -> int:
        
        count_chk = 0
        string = len(s)
        
        for i in range(string):
            count = 0
            
            for j in range(i,string):
                if s[i] != s[j]:
                    break
                if s[i] == s[j]:
                    count += 1
            
            if count_chk < count:
                count_chk = count
        
        return count_chk   
