class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        ans = {}
        for i,n in enumerate(nums):
            while stk and nums[stk[-1]]<n:
                ind = stk.pop()
                if ind not in ans:
                    ans[ind] = n
            stk.append(i)
        for i,n in enumerate(nums):
            while stk and nums[stk[-1]]<n:
                ind = stk.pop()
                if ind not in ans:
                    ans[ind] = n
            stk.append(i)
        for i in stk:
            if i not in ans:
                ans[i] = -1
        for i in sorted(ans):
            yield ans[i]