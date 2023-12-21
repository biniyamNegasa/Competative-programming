class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans='-1'
        for i in range(len(num)-2):
            n = num[i:i+3]
            if n[0]==n[1]==n[2] and int(n)>int(ans):
                if not int(n):
                    ans='000'
                else:
                    ans=n
        return ans if ans!='-1' else ''