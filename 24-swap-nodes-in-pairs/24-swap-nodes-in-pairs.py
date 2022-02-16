# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if (head is None or head.next is None):
            return head
        
        root = ListNode(-1)
        tail = root
        
        temp = head
        
        while(temp):
            
            end = temp
            prev = None
            curr = temp
            nexa = temp
            count = 2
            while(nexa and count):
                
                count -=1
                
                nexa = nexa.next
                curr.next = prev
                prev = curr
                curr = nexa
            
            tail.next = prev
            tail = end
            temp = nexa
        
        return root.next
                
        