class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        res = list()
        
        for i in nums:
            res.append(sum(i > j for j in nums))
        
        return res
                
