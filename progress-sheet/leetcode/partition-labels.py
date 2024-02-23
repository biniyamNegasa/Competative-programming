class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch].append(i)
        for i in range(len(s)-1,-1,-1):
            if len(dic[s[i]])<2:
                dic[s[i]].append(i)
        ans = []
        start = 0
        end = dic[s[0]][1]
        for ch in dic:
            a=dic[ch][0]
            b=dic[ch][1]
            if a>end:
                ans.append(end-start+1)
                start = a
                end = b
            elif b>end:
                end = b
        ans.append(end-start+1)
        return ans
