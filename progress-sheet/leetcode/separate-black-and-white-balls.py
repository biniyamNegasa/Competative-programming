class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        j = 0
        for i, bit in enumerate(s):
            if bit=='0':
                ans += i-j
                j+=1
        return ans