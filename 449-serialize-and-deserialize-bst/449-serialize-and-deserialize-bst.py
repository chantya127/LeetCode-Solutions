# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        def solve(root):
            if (root is None):
                ans[0] += '-1'
                return
            
            ans[0] += str(root.val) + "#"
            solve(root.left)
            solve(root.right)
        
        ans = [""]
        
        solve(root)
        return ans[0]
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        
        def solve(idx , size):
            
            if (idx[0] == size):
                return None
            
            if (data[idx[0]] == '#'):
                idx[0] +=1
                
            if (data[idx[0]] == '-'):
                idx[0] +=2
                return None
            
            
                
            curr_num = 0
            
            while(idx[0] < size and data[idx[0]].isdigit()):
                
                curr_num = curr_num *10 + int(data[idx[0]])
                idx[0] +=1
            
            curr_node = TreeNode(curr_num)
            curr_node.left = solve(idx , size)
            curr_node.right =solve(idx ,size)
            
            return (curr_node)
            
        
        # print(data)
        return solve([0],len(data))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans