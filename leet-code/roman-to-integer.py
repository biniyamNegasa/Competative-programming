class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i+1 != len(s):
                if (s[i]=='I' and s[i+1]=='V') or (s[i]=='I' and s[i+1]=='X') or (s[i]=='X' and s[i+1]=='L') or (s[i]=='X' and s[i+1]=='C') or (s[i]=='C' and s[i+1]=='D') or (s[i]=='C' and s[i+1]=='M'):
                    ans-=dic[s[i]]
                else:
                    ans+=dic[s[i]]
            else:
                ans+=dic[s[i]]
        return ans