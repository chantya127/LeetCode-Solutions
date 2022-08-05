# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def solve(root , ans):
            
            if (root is None):
                return (0)
            
            left_sum = solve(root.left , ans)
            right_sum = solve(root.right , ans)
            
            child_max = max(left_sum , right_sum) 
            curr_max = max(root.val , child_max + root.val , root.val + left_sum + right_sum)
            
            ans[0] = max(ans[0] , curr_max)
            
            return max(child_max + root.val , root.val)
            
            
        
        ans = [float('-inf')]
        
        solve(root , ans)
        
        return (ans[0])