# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        stack1 = []
        stack2 = []
        
        temp = root
        while(temp):
            stack1.append(temp)
            temp = temp.left
        
        temp = root
        while(temp):
            stack2.append(temp)
            temp = temp.right
        
        while(stack1 and stack2):
            
            node1 ,node2 = stack1[-1] , stack2[-1]
            
            summe = node1.val + node2.val
            
            if(summe == k) and node1.val != node2.val:
                return True
            
            elif(summe > k):
                node2 = stack2.pop()
                
                temp = node2.left
                while(temp):
                    stack2.append(temp)
                    temp = temp.right
            
            else:
                node1 = stack1.pop()
                temp = node1.right
                while(temp):
                    stack1.append(temp)
                    temp = temp.left
        
        return False