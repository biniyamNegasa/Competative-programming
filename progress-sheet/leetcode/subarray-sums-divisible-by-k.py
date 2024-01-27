class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr = 0
        ans = 0
        for n in nums:
            curr += n
            ans += dic[curr%k]
            dic[curr%k]+=1
        return ans