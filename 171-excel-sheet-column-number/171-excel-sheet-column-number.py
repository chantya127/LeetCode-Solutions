class Solution:
    def titleToNumber(self, title: str) -> int:
        
        # columns = [chr(i+65) for i in range(26)]
        
        # print(ord('Y') -ord('A') + 1 + (ord('Z') -ord('A') + 1)*26)
        
        num = 0
        size = len(title)
        ptr = size-1
        power = 0
        
        while(ptr >=0):
            
            char = title[ptr]
            
            idx = ord(char) -ord('A')+1
            num += (26**power)*idx 
            ptr -=1
            power +=1
        
        return num
            