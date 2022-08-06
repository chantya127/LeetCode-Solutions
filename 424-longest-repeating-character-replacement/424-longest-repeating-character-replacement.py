class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_char_count =defaultdict(int)
        
        maxi = 0
        
        left = 0
        ans = 0
        size = len(s)
        for right in range(size):
            
            curr_char = s[right]
            max_char_count[curr_char] +=1
            
            maxi = max(maxi , max_char_count[curr_char])
            
            letter_change = right-left+1 - maxi
            if (letter_change > k):
                prev_char = s[left]
                left +=1
                max_char_count[prev_char] -=1
            
            ans = max(ans , right-left+1)
        
        return ans