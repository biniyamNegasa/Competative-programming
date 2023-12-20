class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 15
        while 3**power>n:
            power-=1
        ans=0
        while power>-1:
            if ans + 3**power<= n:
                ans += 3**power
            power-=1
        return ans==n