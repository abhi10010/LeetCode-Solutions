class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        startValue, s, i, flag = 1, 1, 0, 0
        
        while flag != 1:
            startValue += nums[i]
            
            if startValue < 1:
                startValue = s + 1
                i, s = 0, s + 1
                continue
            else:
                i += 1
            
            if i == len(nums):
                flag = 1
                break
        
        return s  
