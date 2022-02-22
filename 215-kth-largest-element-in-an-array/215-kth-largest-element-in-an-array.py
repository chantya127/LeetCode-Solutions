from heapq import heappush as push , heappop as pop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            
            push(heap ,num)
            if(len(heap) > k):
                pop(heap)
        
        return heap[0]