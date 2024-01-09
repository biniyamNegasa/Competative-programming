class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = nums.count(val)
        L = 0
        for R in range(len(nums)):
            if nums[L]==val:
                if nums[R]!= val:
                    nums[L], nums[R] = nums[R], nums[L]
                    L += 1
            else:
                L+=1
        return len(nums)-k