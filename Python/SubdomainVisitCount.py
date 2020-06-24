class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        res = collections.Counter()
        
        for domain in cpdomains:
            
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            
            for i in range(len(frags)):
                res[".".join(frags[i:])] += count
        
        return ["{} {}".format(cnt, dom) for dom, cnt in res.items()]
