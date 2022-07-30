# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush as push , heappop as pop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        heap = []
        size = len(lists)
        if (size == 0):
            return None
        
        for idx in range(size):
            
            if  (lists[idx]):
                push(heap, (lists[idx].val,idx ,lists[idx]))
        
        mhead = ListNode(-1)
        mtail = mhead
                
        while(heap):
            
            val ,_,node = pop(heap)
            mtail.next = node
            mtail = mtail.next
            
            if (node.next):
                idx +=1
                push(heap, (node.next.val,idx , node.next))
            
            mtail.next = None
            
        return mhead.next