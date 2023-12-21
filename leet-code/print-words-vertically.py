class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(" ")
        mx = len(sorted(words, key=lambda x: len(x))[-1])
        temp = [[' ' for _ in range(len(words))] for _ in range(mx)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                temp[j][i]=words[i][j]
        ans=[]
        for w in temp:
            ans.append(''.join(w).rstrip())
        return ans