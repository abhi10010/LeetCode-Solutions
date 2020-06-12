class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*n*2
        i,j = 0, 0
        while i < n and j < n*2:
            res[j] = nums[i]
            res[j+1] = nums[i+n]
            i+=1
            j+=2
        return res
