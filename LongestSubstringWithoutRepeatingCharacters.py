class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx=0
        ls=[]
        for R in range(len(s)):
            while ls and s[R] in ls:
                ls.pop(0)
            ls.append(s[R])
            mx=max(len(ls),mx)
        return mx
