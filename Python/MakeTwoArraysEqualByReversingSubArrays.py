class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        if len(target) == len(arr):
            
            for i in range(len(arr)):
                if arr[i] not in target or arr.count(arr[i]) != target.count(arr[i]):
                    return False
            
            return True
        
        return False
