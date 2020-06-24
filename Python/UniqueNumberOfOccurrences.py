class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return len(set([y for x,y in Counter(arr).most_common()]))==len([y for x,y in Counter(arr).most_common()])
