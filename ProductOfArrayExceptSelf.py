class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        pre=[1]
        suf=[1]
        n=len(nums)-1
        for i in range(n+1):
            pre.append(pre[-1]*nums[i])
            suf.append(suf[-1]*nums[n-i])
        suf=suf[:-1]
        suf=suf[::-1]
        for i in range(n+1):
            ans.append(pre[i]*suf[i])
        return ans
