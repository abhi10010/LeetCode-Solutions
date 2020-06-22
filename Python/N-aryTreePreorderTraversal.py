class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if root is None: 
            return []
        
        else:
            res = [root.val]

            for c in root.children:
                res.extend(self.preorder(c))

        return res
