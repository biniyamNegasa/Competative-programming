class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum=0
        dic={0:1}
        n=0
        for num in nums:
            preSum+=num
            if preSum-k in dic:
                n+=dic[preSum-k]
            if preSum in dic:
                dic[preSum]+=1
            else:
                dic[preSum]=1
        return n
