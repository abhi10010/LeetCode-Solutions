class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        k = paths[0][1]
        i = 0
        
        while i<len(paths):
            
            if k in paths[i][0]:
                k = paths[i][1]
                i = 0
            
            i+=1
        
        return k
