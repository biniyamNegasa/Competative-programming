class Solution:
    def sortSentence(self, s: str) -> str:
        v = s.split()
        v.sort(key=lambda x: int(x[-1]))
        for i, chars in enumerate(v):
            v[i]=chars[:-1]
        return ' '.join(v)