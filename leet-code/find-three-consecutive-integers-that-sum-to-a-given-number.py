class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=(num-3)/3
        ans=int(n)
        if n==ans:
            return [ans, ans+1, ans+2]
        else:
            return []