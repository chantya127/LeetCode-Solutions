class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        seti = set(words)
        for word in words:
            for i in range(1,len(word)):
                seti.discard(word[i:])
        
        return sum(len(w)+1 for w in seti)