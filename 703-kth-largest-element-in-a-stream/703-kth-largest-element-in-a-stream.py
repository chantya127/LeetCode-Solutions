from heapq import heappush as push, heappop as pop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.heap = []
        self.limit= k
        for num in nums:
            
            push(self.heap , num)
        
        
    def add(self, val: int) -> int:
        
        push(self.heap , val)
        
        while(len(self.heap) > self.limit):
            
            pop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)