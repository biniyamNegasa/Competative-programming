class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[\W_]+', '', s).lower()
        for i in range(len(s)):
            if s[i]!=s[-1*(i+1)]:
                return False
        return True
