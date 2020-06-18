class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        
        for i in words:
            a = ""
            
            for j in range(len(i)):
                x = ord(i[j]) - 97
                a += m[x]
            
            res.append(a)
        
        return len(set(res))
        
