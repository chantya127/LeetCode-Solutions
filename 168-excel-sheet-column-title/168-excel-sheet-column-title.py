class Solution:
    def convertToTitle(self, title: int) -> str:
        
        columns = [chr(i+65) for i in range(26)]
        ans = ""
        while(title):
            rem = (title)%26
            
            if (rem == 0):
                rem = 25
            
            else:
                rem -=1
            
            ans += columns[rem]
            
            title = (title-1)//26
        
        return ans[::-1]