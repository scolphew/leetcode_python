class Codec:
    def __init__(self):
        self.s2l = {}
        self.l2s = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.l2s:
            return f"http://tinyurl.com/{self.l2s[longUrl]}"
        i = str(hex(id(longUrl)))[-6:]
        self.l2s[longUrl] = i
        self.s2l[i] = longUrl
        return f"http://tinyurl.com/{i}"

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        i = shortUrl[-6:]
        return self.s2l[i]


if __name__ == '__main__':
    codec = Codec()
    s = "https://leetcode.com/problems/design-tinyurl"
    print(codec.encode(s))
    print(codec.decode(codec.encode(s)))
    print(codec.decode(codec.encode(s)))
