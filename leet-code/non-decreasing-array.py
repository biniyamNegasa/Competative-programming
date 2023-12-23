class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stk=[]
        for n in nums:
            while stk and stk[-1]>n:
                stk.pop()
            stk.append(n)
        stk2=[]
        for n in nums[::-1]:
            while stk2 and stk2[-1]<n:
                stk2.pop()
            stk2.append(n)
        val=max(len(stk),len(stk2))
        return val+1>=len(nums)