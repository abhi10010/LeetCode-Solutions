class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = list()
        m = max(target)
        
        for i in range(n):
            
            if i + 1 in target and i + 1 <= m:
                res.append('Push')
            elif i + 1 not in target and i + 1 <= m:
                res.append('Push')
                res.append('Pop')
            elif i + 1 > m:
                continue
        
        return res
