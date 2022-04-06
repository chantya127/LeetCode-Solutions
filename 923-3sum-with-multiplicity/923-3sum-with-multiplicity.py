class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        ans = 0
        mod = 10**9 +7
        
        dd = defaultdict(int)
        
        size = len(arr)
        
        for idx in range(size):
            
            curr = arr[idx]
            
            ans = (ans + dd[target-curr])%mod
            
            for j in range(0,idx):
                
                temp = arr[j] + curr
                dd[temp] +=1
        
        return ans