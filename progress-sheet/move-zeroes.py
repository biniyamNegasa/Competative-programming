class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = 1
        while R<len(nums):
            if not nums[L] and nums[R]:
                nums[L], nums[R] = nums[R], nums[L]
                L+=1
            elif nums[L]:
                L+=1
            R+=1
        