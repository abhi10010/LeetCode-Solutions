class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        for i in range(len(sentence.split(' '))):
            if searchWord in sentence.split(' ')[i] and searchWord[0] == sentence.split(' ')[i][0]:
                return i+1
            
        return -1
