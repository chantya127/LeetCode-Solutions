# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def solve(pre_idx , low , high):
            
            if (pre_idx  == size or low > high):
                return None
            
            if (low == high):
                
                node =  TreeNode(preorder[pre_idx[0]])
                pre_idx[0] +=1
                
                return node
            
            data = preorder[pre_idx[0]]
            root = TreeNode(data)
            
            idx = mapping_inorder[data]
            
            pre_idx[0] +=1
            
            root.left = solve(pre_idx , low,idx-1)
            root.right= solve(pre_idx , idx+1, high)
            
            return root
            
            
        mapping_inorder = {}
        size = len(inorder)
        for idx in range(size):
            val = inorder[idx]
            mapping_inorder[val] = idx
        
        root = solve([0] , 0,size-1)
        return root