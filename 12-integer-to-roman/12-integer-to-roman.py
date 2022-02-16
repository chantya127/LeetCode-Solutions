class Solution:
    def intToRoman(self, num: int) -> str:
        
        ans = ""
        
        number = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        pos = len(number) -1
        ans = ""
        
        while(num):
            
            quo = num//number[pos]
            num = num%number[pos]
            
            if (quo > 0):
                
                ans += roman[pos]*quo
            
            pos -=1
            
        return ans