class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        n = len(nums)
        res = [-1] * n
        
        for i in range(n):
            
            if res[index[i]] == -1:   
                res[index[i]] = nums[i]
            else:
                res = res[:index[i]] + [nums[i]] + res[index[i]:n-1]
        
        return res
