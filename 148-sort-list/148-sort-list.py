# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
        
    def merge(self , first , sec):

        if not first:
            return sec
        
        if not sec:
            return first
        
        res = None
        
        if first.val <= sec.val:
            res = first
            res.next = self.merge(first.next , sec)
            
        else:
            res = sec
            res.next = self.merge(first , sec.next)
        
        return res
    
    def sortList(self, head: ListNode) -> ListNode:
        

        if (head is None):
            return head

        def mergesort(head , tail):
            

            if (tail.next == head):
                return None
            
            if (head == tail):
                return head

            slow , fast = head , head.next
            while(fast and fast.next):
                
                slow =slow.next
                fast = fast.next.next

            mid = slow
            nexa = mid.next
            mid.next = None
            first = mergesort(head , mid)
            sec = mergesort(nexa , tail)
            return self.merge(first , sec)

        temp = head
        while(temp.next):
            temp = temp.next

        return mergesort(head , temp)    
        