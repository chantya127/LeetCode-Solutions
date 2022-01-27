from heapq import heappush as push , heappop as pop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], prob: List[float], start: int, end: int) -> float:
        
        dp = [0.000]*(n)
        dp[start] = 1.0
        graph = defaultdict(list)
        vis = set()
        for idx in range(len(edges)):
            src ,dest = edges[idx][0] , edges[idx][1]
            wt = prob[idx]
            
            graph[src].append((dest,wt))
            graph[dest].append((src,wt))
        
        heap = []
        push(heap , (-1.0,start))
        
        while(heap):
            
            curr_prob , node = pop(heap)
            curr_prob = -curr_prob
            # print(node)
            
            if (node == end):
                return (curr_prob)
            
            for adj,wt in graph[node]:
                
                if (dp[adj] < wt*(curr_prob)):
                    
                    dp[adj] = wt*(curr_prob)
                    push(heap , (-dp[adj] , adj))
        
        return (0.0)