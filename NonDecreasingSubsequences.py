class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]
        n=len(nums)
        def rec(i):
            if i==n:
                if len(cur)>=2 and cur not in ans:
                    ans.append(cur[:])
                return
            if (cur and nums[i]>=cur[-1]) or not cur:
                cur.append(nums[i])
                rec(i+1)
                cur.pop()
            rec(i+1)
        rec(0)
        return ans
