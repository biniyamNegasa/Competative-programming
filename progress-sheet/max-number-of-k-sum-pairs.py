class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        L = 0
        R = len(nums)-1
        while L<R:
            if nums[L]+nums[R]==k:
                count += 1
                L += 1
                R -= 1
            elif nums[L]+nums[R]>k:
                R -= 1
            else:
                L += 1
        return count