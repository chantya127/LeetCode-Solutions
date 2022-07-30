from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        ans = defaultdict(list)
        
        for word in strs:
            
            sorted_w = "".join(sorted(word))
            ans[sorted_w].append(word)
        
        return ans.values()