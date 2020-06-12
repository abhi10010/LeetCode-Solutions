class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        x = ""
        
        for i,j in zip(strs[0], strs[-1]):
            if i == j:
                x += i
            else:
                break
        
        return x
        
