class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        for i in range(len(spaces)):
            ans.append(s[spaces[i-1] if i else 0:spaces[i]])
        ans.append(s[spaces[-1]:])
        return ' '.join(ans)