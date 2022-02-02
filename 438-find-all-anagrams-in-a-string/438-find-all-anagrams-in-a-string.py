from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def check(s_map , p_map):
            
            for ch in s_map:
                if (s_map[ch] != p_map[ch]):
                    return False
            
            return True
        
        p_map = defaultdict(int)
        s_map = defaultdict(int)
        
        for ch in p:
            p_map[ch] +=1
        
        n ,m = len(s) , len(p)
        curr = ""
        ans = []
        j = 0
        
        for i in range(n):
            
            ch = s[i]
            s_map[ch] +=1
            
            if (s_map[ch] > p_map[ch]):
                
                while(s_map[ch] > p_map[ch]):
                    
                    prev = s[j]
                    j +=1
                    if (s_map[prev] == 1):
                        s_map.pop(prev)
                    
                    else:
                        s_map[prev] -=1
            
            elif(len(s_map) > len(p_map)):
                
                while(len(s_map) > len(p_map)):
                    
                    prev = s[j]
                    j +=1
                    if (s_map[prev] == 1):
                        s_map.pop(prev)
                    
                    else:
                        s_map[prev] -=1
                
            
            if len(s_map) == len(p_map) and check(s_map , p_map):
                
                start = i - m +1
                ans.append(start)
                
        
        return (ans)
                
            
            