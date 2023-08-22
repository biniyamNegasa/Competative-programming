class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum=[0,]
        for num in nums:
            self.preSum.append(self.preSum[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        l=self.preSum[left]
        r=self.preSum[right+1]
        return r-l

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
