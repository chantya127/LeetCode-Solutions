class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def get_prefix():
            
            prefix = [0]*(need_size)
            p1 = 0
            p2 = 1
            
            
            while(p2 < need_size):
                
                if (needle[p2] == needle[p1]):
                    
                    p1+=1
                    prefix[p2] = p1
                    p2 +=1
                
                else:
                    if (p1 > 0):
                        p1 = prefix[p1-1]
                    
                    else:
                        prefix[p2] = 0
                        p2 +=1
            
            return prefix
        
        if (len(needle) == 0):
            return 0
        
        need_size = len(needle)
        hay_size = len(haystack)
        
        prefix = get_prefix()
        
        hay_ptr,need_ptr = 0,0
        
        while(hay_ptr < hay_size):
            
            if (haystack[hay_ptr] == needle[need_ptr]):
                need_ptr +=1
                hay_ptr +=1
                
                if(need_ptr == need_size):
                    return hay_ptr-need_size
            
            else:
                if (need_ptr > 0):
                    need_ptr = prefix[need_ptr-1]
                
                else:
                    hay_ptr +=1
        
        
        return (-1)