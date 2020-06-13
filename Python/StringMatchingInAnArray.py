class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        res = list()
        
        for i in range(len(words)):
            
            for j in range(len(words)):
                
                if i != j and words[j] in words[i] and words[j] not in res:
                    res.append(words[j])
        
        return res

    
