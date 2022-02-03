class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        size = len(s)
        prev = 0
        
        vis = {}
        ans = 0
        for idx in range(size):
            
            curr = s[idx]
            
            if (curr in vis):
                while(prev <idx):
                    
                    pchar = s[prev]
                    prev +=1
                    vis.pop(pchar)
                    if (pchar == curr):
                        break
            
            vis[curr] = idx
            
            length = idx - prev+1
            ans = max(ans, length)
        
        return (ans)