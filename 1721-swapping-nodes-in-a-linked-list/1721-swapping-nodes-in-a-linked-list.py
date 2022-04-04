# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n1,n2 = None , None
        
        temp = head
        for _ in range(k):
            
            n1 = temp
            temp = temp.next
            
        n2 = head
        while(temp):
            
            temp = temp.next
            n2 = n2.next
        
        if (n1 and n2):
            n1.val , n2.val = n2.val , n1.val
        
        return (head)