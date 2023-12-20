class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        checker=strs[-1]
        ans=""
        for char in checker:
            for word in strs:
                if len(ans+char)>len(word) or ans+char != word[:len(ans+char)]:
                    return ans
            ans+=char
        return ans
            