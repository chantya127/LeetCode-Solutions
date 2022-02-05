# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, heada: ListNode, headb: ListNode) -> Optional[ListNode]:
        
        def get_length(root):
            
            count = 0
            temp = root
            while(temp):
                count +=1
                temp = temp.next
            
            return (count)
        
        l1 = get_length(heada)
        l2 = get_length(headb)
        
        if (l1 > l2):
            diff = l1-l2
            
            while(diff and heada):
                
                heada= heada.next
                diff -=1
        
        elif (l2 > l1):
            
            diff = l2-l1
            while(diff and headb):
                headb = headb.next
                diff -=1
        
        while(heada and headb):
            
            if (heada == headb):
                return (heada)
            
            heada = heada.next
            headb = headb.next
        
        return None
        