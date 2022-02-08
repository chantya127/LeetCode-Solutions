class Solution:
    def addDigits(self, num: int) -> int:
        
        if (num ==0):
            return 0
        
        while(num >=10):
            
            new_num = 0
            while(num >0):
                rem = num%10
                num //=10
                new_num += rem
            
            num = new_num
        
        return (num)