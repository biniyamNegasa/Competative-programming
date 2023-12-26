class Solution:
    def isHappy(self, n: int) -> bool:
        while n>1:
            if n<10 and n!=7:
                return False
            elif n==7:
                return True
            s=[*str(n)]
            temp=0
            for n in s:
                temp += int(n)**2
            n=temp
        return True