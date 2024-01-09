class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        ans = []
        L = 0
        p_c = Counter(p)
        dic = defaultdict(int)
        for i in range(len(p)-1):
            dic[s[i]]+=1
        for R in range(len(p)-1, len(s)):
            dic[s[R]]+=1
            if p_c == dic:
                ans.append(L)
            if dic[s[L]]>1:
                dic[s[L]]-=1
            else:
                del dic[s[L]]
            L+=1
        return ans