class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1={'p', 't', 'e', 'o', 'q', 'r', 'i', 'u', 'w', 'y'} 
        s2={'l', 's', 'k', 'g', 'd', 'a', 'j', 'h', 'f'}
        s3={'b', 'm', 'x', 'v', 'z', 'c', 'n'}
        ans=[]
        for wor in words:
            if self.check(wor.lower(),s1) or self.check(wor.lower(),s2) or self.check(wor.lower(),s3):
                ans.append(wor)
        return ans
    def check(self,word,ss):
        for w in word:
            if w not in ss:
                return False
        return True