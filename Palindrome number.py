class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=str(x)
        c=""
        for i in range(len(b)):
            c+=b[-1*(i+1)]
        return b==c
