# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (head is None or head.next is None):
            return (head)
        
        root = ListNode(-1)
        tail = root    
        
        temp = head
        
        while(temp and temp.next):
            
            if (temp.val == temp.next.val):
                curr = temp.val
                while(temp  and  temp.val == curr):
                    temp = temp.next
                    # print(curr , 'dd')
            
            else:
                tail.next = temp
                tail = temp
                temp = temp.next
                tail.next  =None
        
        if (temp):
            tail.next = temp
            
        return (root.next)
                