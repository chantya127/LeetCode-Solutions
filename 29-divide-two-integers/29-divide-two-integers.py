class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        sign = 1
        
        
        if (dividend<0)^(divisor<0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quo = 0
        while(dividend >= divisor):
            
            temp = divisor
            power = 1
            while(temp <<1 <= dividend):
                
                temp = temp<<1
                power = power <<1
            
            dividend -= temp
            quo += (power)
        
        return quo*sign
            