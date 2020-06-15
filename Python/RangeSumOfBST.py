class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        s = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                if L <= node.val <= R:
                    s += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                
        return s
