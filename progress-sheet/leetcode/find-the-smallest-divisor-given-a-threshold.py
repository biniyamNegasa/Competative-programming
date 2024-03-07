class Solution:
    def tot(self, arr, d):
        count = 0
        for n in arr:
            count+=ceil(n/d)
        return count
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left<=right:
            mid = (left+right)//2
            val = self.tot(nums,mid)
            if val>threshold:
                left = mid+1
            else:
                right = mid-1
        return left