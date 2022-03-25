class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        size = len(costs)
        target_size = size//2
        
        refund = [0]*(size)
        total_cost = 0
        
        for (idx) in range(size):
            
            refund[idx] = (costs[idx][1] - costs[idx][0])
            
            total_cost += costs[idx][0]
        
        refund.sort()
        
        for i in range(target_size):
            total_cost += refund[i]
        
        
        return (total_cost)