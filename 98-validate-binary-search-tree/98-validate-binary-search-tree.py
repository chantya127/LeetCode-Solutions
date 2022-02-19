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
                return (True , float('-inf') , float('inf'))
            
            left_ans , left_max , left_min = solve(root.left)
            
            right_ans , right_max, right_min = solve(root.right)
            
            curr_ans = False
            curr_data = root.val
            
            if (left_ans and right_ans and left_max < curr_data < right_min):
                curr_ans = True
                
            curr_max= max(left_max , curr_data , right_max)
            curr_min = min(left_min , curr_data , right_min)
            
            return (curr_ans , curr_max , curr_min)
            
            
        
        curr_ans , curr_max , curr_min = solve(root)
        return(curr_ans)
        
        