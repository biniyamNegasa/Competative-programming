class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        nums.sort()
        count = Counter(nums)
        ans = 0
        i = 0
        for n in count:
            if i:
                ans += i*count[n]
            i+=1
        return ans