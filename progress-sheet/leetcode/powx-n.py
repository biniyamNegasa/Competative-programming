class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            n = -1*n
            x = 1/x
        if n%2:
            n-=1
            val = self.myPow(x,n//2)
            return x*val*val
        val = self.myPow(x,n//2)
        return val*val