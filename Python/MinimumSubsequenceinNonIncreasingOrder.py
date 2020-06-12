class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        s = sum(nums)/2
        n = 0
        res = list()
        for i in range(len(nums)-1,-1,-1): 
            if n <= s:
                n += nums[i]
                res.append(nums[i])
            else:
                break
        return res
