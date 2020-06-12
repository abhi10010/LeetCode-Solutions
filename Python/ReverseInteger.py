class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x).strip()
        
        if s[0] == '-':
            x = int(s[0] + s[::-1].replace('-', ''))
            if x < (-2 ** 31) :
                return 0
            else:
                return x
        
        else:
            x = int(s[::-1])
            if x > (2 ** 31) - 1:
                return 0
            else:
                return x
