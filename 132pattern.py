class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk=[]
        pmx=float("-inf")
        for n in reversed(nums):
            if n<pmx:
                return True
            else:
                while stk and n>stk[-1]:
                    pmx=stk.pop()
            stk.append(n)
        return False
