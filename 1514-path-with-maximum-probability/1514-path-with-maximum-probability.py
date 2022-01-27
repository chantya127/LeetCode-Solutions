from collections import defaultdict

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
        
        ququ = deque()
        ququ.append(start)
        
        while(ququ):
            node = ququ.popleft()
            if node == end:
                continue
                
            for adj,wt in graph[node]:
                
                if (dp[adj] < dp[node]*wt):
                    
                    dp[adj] = dp[node]*wt
                    
                    ququ.append(adj)
        
        return dp[end]