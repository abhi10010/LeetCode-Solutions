class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        for i in matrix:
            
            min_c = min(i)
            col = i.index(min_c)
            
            if self.maxCol(matrix, col) == min_c:
                
                return [min_c]
            
    
    def maxCol(self, matrix, col):
            
        mx = matrix[0][col]
            
        for i in matrix:
            
            if i[col] > mx:
                mx = i[col]
            
        return mx
    
