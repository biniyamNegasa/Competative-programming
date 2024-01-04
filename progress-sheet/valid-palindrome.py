class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = []
        for ch in s:
            if ch.isalnum():
                v.append(ch.lower())
        L = 0
        R = len(v)-1
        while L<R:
            if v[L]!=v[R]:
                return False
            L+=1
            R-=1
        return True
        