class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = [*palindrome]
        c = [*palindrome]
        if len(s)==1:
            return ""
        for i in range(len(s)):
            if s[i]!='a':
                s[i]='a'
                break
        if self.chk(s):
            c[-1]='b'
            return ''.join(c)
        return ''.join(s)
    def chk(self, s):
        L = 0
        R = len(s)-1
        while L<R:
            if s[L]!=s[R]:
                return False
            L+=1
            R-=1
        return True