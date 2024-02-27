class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums.reverse()
        stk = []
        prev = float('-inf')
        for n in nums:
            while stk and stk[-1]<n:
                prev = stk.pop()
            if n<prev:
                return True
            stk.append(n)
        return False