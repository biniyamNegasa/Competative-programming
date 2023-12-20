class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for num in count:
            temp = count[num]
            ans += temp*(temp-1)//2
        return ans