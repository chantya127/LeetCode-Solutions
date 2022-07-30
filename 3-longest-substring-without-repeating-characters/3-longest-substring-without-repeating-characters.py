from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        dd = defaultdict(int)
        prev_ptr = 0
        
        size = len(s)
        ans = 0
        
        for idx in range(size):
            
            char = s[idx]
            dd[char] +=1
            
            while(prev_ptr <= idx and dd[char] > 1):
                
                prev_char = s[prev_ptr] 
                prev_ptr +=1
                
                if (dd[prev_char] == 1):
                    dd.pop(prev_char)
                
                else:
                    dd[prev_char] -=1
            
            curr_len = idx - prev_ptr+1
            
            # print(idx ,prev_ptr , curr_len)
            ans = max(ans , curr_len)
        
        return (ans)