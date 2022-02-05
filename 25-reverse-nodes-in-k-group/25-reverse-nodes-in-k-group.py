# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_size(root):
            
            count = 0
            
            while(root):
                root = root.next
                count +=1
                
            return (count)
        
        root = ListNode(-1)
        tail = root
        temp = head
        
        size = get_size(head)
        
        while(temp):

            if (size >= k):
                end = temp
                curr,nexa = temp,temp

                count = k
                prev = None
                while(nexa and count):

                    count -=1
                    nexa = nexa.next

                    curr.next = prev
                    prev = curr
                    curr = nexa

                tail.next = prev
                tail = end
                temp = nexa
                size -=k
            
            else:
                tail.next = temp
                break
            
        return (root.next)