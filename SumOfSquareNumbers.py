class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first,second=0,c**0.5//1
        while first**2<=c:
            b=first**2+second**2
            if b==c:
                return True
            elif b<c:
                first+=1
            else:
                second-=1
        return False
