class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        stk=[]
        for num in nums:
            if not num:
                ans = max(ans, len(stk))
                while stk:
                    stk.pop()
            else:
                stk.append(num)
        ans = max(ans, len(stk))
        return ans