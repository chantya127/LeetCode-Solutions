# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
            
        
        if root is None:
            return 
        
        first , sec = None , None
        prev = TreeNode(float('-inf'))
        
        while(root):
            
            if (root.left is None):
                
                if (prev.val >= root.val):
                    if (not first):
                        first = prev
                    
                    sec = root
                
                prev = root
                root = root.right
            
            else:
                curr = root.left
                while(curr.right and curr.right != root):
                    curr = curr.right
                
                if (curr.right is None):
                    curr.right = root
                    root = root.left
                
                else:
                    curr.right = None
                    
                    if (prev.val >= root.val):
                        if (not first):
                            first = prev
                    
                        sec = root
                    
                    prev = root    
                    root = root.right
                    
        first.val , sec.val = sec.val  ,first.val