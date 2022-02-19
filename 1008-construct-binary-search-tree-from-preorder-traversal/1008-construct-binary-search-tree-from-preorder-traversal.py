# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def solve(pre_idx , low , high):
            
            if(pre_idx[0] == size):
                return None
            
            curr = preorder[pre_idx[0]]
            
            if(low <= curr <= high):
                
                root = TreeNode(curr)
                pre_idx[0] +=1
                
                root.left = solve(pre_idx , low , curr-1)
                root.right = solve(pre_idx , curr+1 , high)
                
                return (root)
            
            else:
                return None
            
            
        
        size = len(preorder)
        pre_idx = [0]
        
        root = solve(pre_idx , float('-inf') ,float('inf'))
        
        return root