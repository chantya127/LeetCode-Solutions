class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        # [3,3,4,5]
        
        people.sort()
        boats = 0
        
        low , high = 0 , len(people)-1
        
        while(low < high):
            
            val = people[low] + people[high]
            
            if (val <= limit):
                low +=1
                
            high -=1
            boats +=1
        
        if (low == high):
            boats +=1
        
        return (boats)
            
        
        
        
        