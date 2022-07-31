from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        target_map = defaultdict(int)
        string_map = defaultdict(int)
        
        
        prev_ptr = 0
        curr_count, desired_count = 0,0 
        start_idx , end_idx ,min_len = 0, 0 , float('inf')
        size = len(s)
        
        for ch in t:
            target_map[ch] += 1
            desired_count +=1
        
        
        for idx in range(size):
            
            curr_char = s[idx] 
            string_map[curr_char] +=1
            
            
            
            if (string_map[curr_char] <= target_map[curr_char]):
                curr_count +=1
            
            
            
            while(curr_count == desired_count):
                
                curr_len = idx - prev_ptr +1
                if (curr_len < min_len):
                    min_len = curr_len
                    start_idx = prev_ptr
                    end_idx = idx
                
                prev_char = s[prev_ptr]
                prev_ptr +=1
                
                string_map[prev_char] -=1
                
                if (string_map[prev_char] < target_map[prev_char]):
                    curr_count -=1
        
        if (min_len) == float('inf'):
            return ""
        
        return s[start_idx : end_idx+1]