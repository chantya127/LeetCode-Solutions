# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            
            if (root is None):
                
                return (True , float('-inf') , float('inf'),0)
            
            lans , lmax , lmin , lsum = solve(root.left)
            
            rans , rmax , rmin , rsum = solve(root.right)
            
            curr = root.val
            curr_ans = False
            
            if (lans and rans and lmax < curr < rmin):
                
                ans[0] = max(ans[0] , curr + lsum + rsum)
                
                curr_ans = True
                
            
            curr_min = min(lmin , rmin , curr)
            curr_max= max(rmax , lmax , curr)
            curr_sum = root.val + lsum + rsum
            
            return (curr_ans , curr_max , curr_min , curr_sum)
            
        
        ans = [0]
        
        curr_ans , curr_max , curr_min , curr_sum = solve(root)
        
        return ans[0]