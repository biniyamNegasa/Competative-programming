class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [0]
        for n in nums:
            pre_sum.append(pre_sum[-1]+n)
        for i in range(len(nums)):
            prev = pre_sum[i]
            nxt = pre_sum[-1]-pre_sum[i+1]
            if prev==nxt:
                return i
        return -1
                   