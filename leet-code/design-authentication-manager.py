class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dic={}
        self.t=timeToLive        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and self.dic[tokenId]+self.t>currentTime:
            self.dic[tokenId]=currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c=0
        for n in self.dic:
            if self.dic[n]+self.t>currentTime:
                c+=1
        return c
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)