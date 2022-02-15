class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        
        ptr = 0
        size = len(s)
        while(ptr < size):
            
            if (s[ptr] != " "):
                
                curr = ""
                while(ptr <size and s[ptr] != " "):

                    curr += s[ptr]
                    ptr +=1

                stack.append(curr)
            
            else:
                ptr +=1
        
        ans = ""
        
        while(stack):
            
            word = stack.pop()
            ans += word
            
            if (len(stack) != 0):
                ans += " "
        
        return (ans)