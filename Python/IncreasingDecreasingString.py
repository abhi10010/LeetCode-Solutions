 dict = {}
        for i in s:
            
            if i not in dict:
                dict[i] = 1
            
            else:
                dict[i] += 1
        
        
        lst = sorted(dict.keys())
        index = 0
        res = ''
        
        while True:
            flag = -1
            
            for x in lst:
                
                if dict[x] > 0:
                    res += x
                    dict[x] -= 1
            
            for x in lst[::-1]:
                
                if dict[x] > 0:
                    res += x
                    dict[x] -= 1
            
            for i in dict:
                
                if dict[i] > 0:
                    flag = 1
                    break
            
            if flag == 1:
                
                continue
            
            else:
                break
                
        return res
