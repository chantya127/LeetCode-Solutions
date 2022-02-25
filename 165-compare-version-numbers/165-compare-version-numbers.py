class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        
        for idx in range(max(len(v1) , len(v2))):
            
            val1 = 0 if idx >= len(v1) else v1[idx]
            val2 = 0 if idx>=len(v2) else v2[idx]
            
            if (val1 > val2):
                return 1
            
            if (val2 > val1):
                return -1
        
        return 0