import string
class Codec:
    def __init__(self):
        self.counter = 0
        self.long_to_short = {}
        self.short_to_long = {}
        self.letters = string.ascii_letters + string.digits
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def id_to_base62():
            n = self.counter
            
            res = ''
            count = 0
            while True:
                res = self.letters[n%62] + res
                n = n//62
                if n ==0:
                    break
                    
                
            return "http://tinyurl.com/" + res  
            
        suffix = id_to_base62()
        if longUrl not in self.long_to_short.keys():
            
            self.long_to_short[longUrl] = suffix
            self.short_to_long[suffix] = longUrl
            self.counter+=1
        
        return suffix
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        if shortUrl in self.short_to_long.keys():
            return self.short_to_long[shortUrl]
        return None
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))