class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        mat = [[0 for i in range(m)] for i in range(n)]
        
        for i in indices:
            r, c = i
            
            for j in range(m):
                mat[r][j] += 1
            
            for k in range(n):
                mat[k][c] += 1
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                
                if mat[i][j] % 2 == 1:
                    count+=1
        
        return count
        
       
            
