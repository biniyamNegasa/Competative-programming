class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        L = 0
        count = 0
        for i in range(k-1):
            if s[i] in vowels:
                count+=1
        for R in range(k-1, len(s)):
            if s[R] in vowels:
                count+=1
            mx = max(mx, count)
            if s[L] in vowels:
                count-=1
            L+=1
        return mx