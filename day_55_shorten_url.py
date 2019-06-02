#shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
#restore(short), which expands the shortened string into the original url. 
#If no such shortened string exists, return null.
    
#class URL_Shortener:
#    url2id = {}
#    id = 62
#    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    base62 = len(characters)
#    
#    def shorten_url(self, original_url):
#        if original_url in self.url2id:
#            id = self.url2id[original_url]
#            shorten_url = self.encode(id)
#        else:
#            self.url2id[original_url] = self.id
#            shorten_url = self.encode(self.id)
#            self.id += 1
#        
#        return "short_url.com/"+str(shorten_url)
#    
#    def encode(self, id):
#        ret = []
#        while id > 0:
#            val = id % self.base62
#            ret.append(self.characters[val])
#            id = id // self.base62
#           
#        return "".join(ret[::-1])

#if __name__ == "__main__":
#    shortener = URL_Shortener()
#    print(shortener.shorten_url("naver.com"))
#    print(shortener.shorten_url("naver.com"))
#    print(shortener.shorten_url("daum.net"))
#    print(shortener.shorten_url("google.com"))

url2id = {}
id = 12313213
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
base62 = len(characters)
original_url = "https://www.naver.com/"
shortenUrl = ""
div = []

def shorten_url(original_url):
    def _encode(id):
        ret = []
        while id > 0:
            div_val, val = divmod(id, base62)
            if len(div) == 0:
                div.append(div_val)
            ret.append(characters[val])
            id = id // base62
            
        return "".join(ret[::-1])
    
    shortenUrl = _encode(id)
    return shortenUrl

def restore(shortenUrl):
    shortenUrl = shortenUrl[::-1]
    result = ""
    val = characters.index(shortenUrl[0])
    result += (str(val + div[0] * base62))
    
    return result
    
shortenUrl = shorten_url(original_url)
print(original_url + shortenUrl)
print("id : {0}".format(id))
print(restore(shortenUrl))