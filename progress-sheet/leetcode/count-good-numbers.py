class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        val = n//2
        if n%2:
            return (5*self.calc(val))%MOD
        else:
            return self.calc(val)%MOD
    def calc(self, n):
        MOD = 10**9 + 7
        if not n:
            return 1
        if n==1:
            return 20
        val = self.calc(n//2)
        if n%2:
            return (20*val*val)%MOD
        else:
            return (val*val)%MOD