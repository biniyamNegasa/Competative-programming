class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        ans = 0
        odd = 1
        for val in dic.values():
            if val%2==0 or odd:
                ans+=val
                if val%2:
                    odd-=1
            else:
                ans += val-1
        return ans