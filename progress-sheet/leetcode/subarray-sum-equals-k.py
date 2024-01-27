class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dic = defaultdict(int)
        dic[0]+=1
        curr = 0
        for i,n in enumerate(nums):
            curr+=n
            ans += dic[curr-k]
            dic[curr]+=1
        return ans