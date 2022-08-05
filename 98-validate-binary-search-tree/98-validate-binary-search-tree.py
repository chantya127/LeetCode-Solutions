# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root):
            if (root is None):
                return (True,float('inf') , float('-inf'))
            
            
            left_is_bst , left_min, left_max = solve(root.left)
            
            
            if (not left_is_bst or root.val <= left_max):
                return (False,float('inf') , float('-inf'))
                        
            
            right_is_bst, right_min, right_max = solve(root.right)
            if (not right_is_bst or root.val >= right_min):
                return (False,float('inf') , float('-inf'))
            
            curr_max = max(root.val , left_max ,right_max)
            curr_min = min(root.val , left_min , right_min)
            
            
            
            return (True , curr_min ,curr_max)

        
        ans,_,_ = solve(root)
        
        return (ans)
        