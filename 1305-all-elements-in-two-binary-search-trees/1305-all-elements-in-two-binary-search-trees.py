# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, r1: TreeNode, r2: TreeNode) -> List[int]:
        
        
        def push(stack , node):
            if (node is None):
                return
            
            while(node):
                stack.append(node)
                node = node.left
        
            
        if (r1 is None and r2 is None):
            return []

        s1 , s2 = [] , []
        ans = []
        temp = r1
        while(temp):

            s1.append(temp)
            temp = temp.left

        temp = r2
        while(temp):
            s2.append(temp)
            temp= temp.left

        ans = []
        while(s1 or s2):

            v1,v2 = float('inf'),float('inf')

            if (s1):
                v1 = s1[-1].val

            if (s2):
                v2= s2[-1].val
            
            # print(v1,v2 , ans)
            if(v2 > v1):

                ans.append(v1)
                if (s1):
                    
                    node = s1.pop()
                    push(s1 , node.right)

            elif (v2 < v1):
                ans.append(v2)
                if (s2):
                    node = s2.pop()
                    push(s2 , node.right)

            elif (v1 != float('inf')):
                ans.append(v1)
                ans.append(v2)
                if (s1):
                    node1 = s1.pop()
                    push(s1 , node1.right)
                
                if (s2):
                    node2 = s2.pop()
                    push(s2 , node2.right)

        return (ans)