class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root:
            
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        
        return root
