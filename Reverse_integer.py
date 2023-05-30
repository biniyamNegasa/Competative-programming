class Solution:
    def reverse(self, x: int) -> int:
        if x!=0:
            sign=int(x/abs(x))
            x=[*(str(abs(x)))]
            m=[]
            for i in range(len(x)):
                 m+=x[-1*(i+1)]
            m=int(''.join(m))
            return sign*m if sign*m <= 2**31-1 and sign*m>= -2**31 else 0
        return x
