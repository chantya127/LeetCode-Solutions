from heapq import heappush as push , heappop as pop


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        nums = [int(num) for num in nums]
        
        heap = []
        size = len(nums)
        for idx in range(size):
            
            curr = nums[idx]
            push(heap,curr)
            if (len(heap) > k):
                pop(heap)

        return str(heap[0])