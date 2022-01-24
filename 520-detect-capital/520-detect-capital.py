class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        flag = 0
        
        for ch in word:
            
            if(ch.isupper()):
                flag +=1
            
        
        if (flag == 0 or flag == len(word)) or (flag == 1 and word[0].isupper()):
            return True
        
        return (False)