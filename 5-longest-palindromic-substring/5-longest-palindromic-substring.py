class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start_idx , end_idx = 0,0
        max_len = 1
        
        size = len(s)
        
        for idx in range(size):
            
            # even start
            
            ptr1 = idx
            ptr2 = idx +1
            
            while(ptr1 >=0 and ptr2 < size and s[ptr1] == s[ptr2]):
                ptr1 -=1
                ptr2 += 1
            
            curr_len = ptr2 -ptr1 -1
            if (curr_len > max_len):
                start_idx  = ptr1 +1 
                max_len = curr_len
            
            
            # odd_start
            ptr1 = idx-1
            ptr2 = idx+1
            
            while(ptr1 >=0 and ptr2 < size and s[ptr1] == s[ptr2]):
                ptr1 -=1
                ptr2 +=1
            
            curr_len = ptr2-ptr1-1
            if (curr_len > max_len):
                start_idx  = ptr1+1
                max_len = curr_len
            
            
        print(start_idx , end_idx , max_len)
        return s[start_idx:start_idx+max_len]
            