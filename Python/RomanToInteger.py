class Solution:
    def romanToInt(self, s: str) -> int:
        
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        y = 0
        i = len(s) - 1
        
        while i>-1:
            if s[i] == 'V' and s[i-1] == 'I' and i!=0:
                y += 4
                i -= 2
            elif s[i] == 'X' and s[i-1] == 'I' and i!=0:
                y += 9
                i -= 2
            elif s[i] == 'L' and s[i-1] == 'X' and i!=0:
                y += 40
                i -= 2
            elif s[i] == 'C' and s[i-1] == 'X' and i!=0:
                y += 90
                i -= 2
            elif s[i] == 'D' and s[i-1] == 'C' and i!=0:
                y += 400
                i -= 2
            elif s[i] == 'M' and s[i-1] == 'C' and i!=0:
                y += 900
                i -= 2
            else:
                y += val[s[i]]
                i -= 1
        
        return y
