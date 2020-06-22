class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        if root is None:
            return res
        
        else:
            stack = [root]
            
            while stack:
                node = stack[-1]
                
                if node.children:
                    
                    while node.children:
                        stack.append(node.children.pop())
                
                else:
                    res.append(stack.pop().val)
        return res
