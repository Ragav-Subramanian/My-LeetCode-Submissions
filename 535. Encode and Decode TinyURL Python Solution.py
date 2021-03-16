class Codec:

    def __init__(self):
        self.shorttolong={}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short=str(hash(longUrl))
        self.shorttolong[short]=longUrl
        return "http://tinyurl.com/"+short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shorttolong[shortUrl[19:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))