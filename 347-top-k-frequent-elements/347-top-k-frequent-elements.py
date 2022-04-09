from heapq import heappush as push ,heappop as pop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        counting = defaultdict(int)
        for num in nums:
            counting[num] +=1
        
        heap = []
        
        for (key ,val) in counting.items():
            
            push(heap , (val , key))
            
            if (len(heap) > k):
                pop(heap)
            
        ans = []
        for (key,val) in heap:
            ans.append(val)
        
        return ans