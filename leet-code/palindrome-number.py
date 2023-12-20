class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=x
        power=-1
        while y:
            y//=10
            power+=1
        ans=0
        temp=x
        while temp:
            ans+=temp%10 * 10**power
            temp//=10
            power-=1
        return ans==x
            