class Solution:
    def myAtoi(self, s: str) -> int:
        
        # if(s == "-91283472332"):
        #     return -2147483648
        
        ans = 0
        ptr = 0
        size = len(s)
        sign = 1
        
        while(ptr < size and s[ptr] == ' '):
            ptr +=1
        
        if (ptr<size and s[ptr] == '-'):
            sign = -1
            ptr+=1
        
        elif (ptr<size and s[ptr] == '+'):
            ptr+=1
        
        while(ptr < size):
            
            curr = s[ptr]
            
            ascii_val = ord(curr) - ord('0')
            
            #print(curr , ascii_val)
            if (0<= ascii_val <=9):
                ans = ans*10 + ascii_val
                ptr+=1
                #flag = 1
            
            else:
                break
        
        
        return max(-2**31 , min(ans*sign , 2**31-1))