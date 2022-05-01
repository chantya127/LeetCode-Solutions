class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def find(string ):
            
            stack = []
            for ch in string:
                if (ch == "#"):
                    if (stack):
                        stack.pop()

                else:
                    stack.append(ch)
            
            return (stack)
        
        s1 = find(s)
        
        s2 = find(t)
        
        return (s1 == s2)