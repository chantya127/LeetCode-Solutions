# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def solve(index , low , high):
            
            
            if (index[0] >= size) or (low > high):
                return None
            
            curr_node = TreeNode(preorder[index[0]])
            index[0] +=1
            
            if (low == high):
                return (curr_node)
            
            node_idx = val_index_mapping[curr_node.val]
            
            curr_node.left =  solve(index , low , node_idx-1)
            curr_node.right = solve(index , node_idx+1 , high)
            
            return (curr_node)
            
        
        val_index_mapping = defaultdict(int)
        for (idx,val) in enumerate(inorder):
            val_index_mapping[val] = idx
            
        size = len(inorder)
        ans = solve([0] , 0, size-1)
        
        # print(ans.left , ans.right)
        
        return (ans)