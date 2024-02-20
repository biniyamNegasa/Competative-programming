class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        nums = [weights[i]+weights[i-1] for i in range(1, len(weights))]
        nums.sort()
        if k-1>0:
            return sum(nums[-(k-1):])-sum(nums[:k-1])
        return 0