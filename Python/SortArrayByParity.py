class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res1, res2 = [], []
        i = 0
        
        while i < len(A):
            
            if A[i] % 2 == 0:
                res1.append(A[i])
            else:
                res2.append(A[i])
            
            i += 1
        
        return res1 + res2
