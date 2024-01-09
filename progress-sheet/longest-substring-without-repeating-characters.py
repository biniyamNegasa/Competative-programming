class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        mx = 0
        L = 0
        for R in range(len(s)):
            while s[R] in dic:
                del dic[s[L]]
                L+=1
            dic[s[R]]=1
            mx = max(mx, R-L+1)
        return mx