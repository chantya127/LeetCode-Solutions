# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        def find(root):
            if (root is None):
                return 0
            
            lsum = find(root.left)
            rsum = find(root.right)
            
            total_sum = lsum + rsum + root.val
            
            counting[total_sum] +=1

            return (total_sum)

        counting = defaultdict(int)

        find(root)

        node,freq = -1,-1
        ans = []

        for key,val in counting.items():
            if (val > freq):
                freq = val
        
        for key,val in counting.items():
            if (val == freq):
                ans.append(key)
        return (ans)