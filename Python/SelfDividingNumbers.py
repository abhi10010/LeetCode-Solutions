class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = [] 
        
        for i in range(left, right+1):
            flag = 0
            s = list(str(i))
            
            for j in s:
                
                if int(j) == 0:
                    flag = 1
                    continue
                
                if i%int(j) != 0:
                    flag = 1
            
            if flag == 0:
                res.append(i)
       
        return res
                  
