class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = max(nums)
        nums.remove(max_val)
        new = nums.copy()
        for i in range(len(nums)):
            nums[i] = nums[i] - max_val
        max_val_2 = new[nums.index(max(nums))]
        return (max_val-1) * (max_val_2-1)
