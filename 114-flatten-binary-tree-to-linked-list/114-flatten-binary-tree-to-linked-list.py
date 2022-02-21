# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
            
           # 2
           #  \       
           #   3       \
           #    \       6
           #     4
           #      \
           #       5
           #        \ 
           #          6

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def solve(root):
            
            if (root is None) or (root.left is None and root.right is  None):
                return root
            
            left = solve(root.left)
            
            right = solve(root.right)
            
            tail = left

            if (tail):
                
                while(tail and tail.right):
                    tail = tail.right
                    
                tail.right = right
            
            else:
                left = right
                
            root.right = left
            root.left = None
            
            return root
            
#         def preorder(root):
            
#             if (root is  not None):
                
#                 print(root.val , end = ' -> ' )
#                 preorder(root.left)
#                 preorder(root.right)
        
        solve(root)
        
        # preorder(root)
        