class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum=0
        dic={0:1}
        n=0
        for num in nums:
            preSum=(preSum+num%k+k)%k
            n+=dic.get(preSum,0)
            dic[preSum]=dic.get(preSum,0)+1
        return n
