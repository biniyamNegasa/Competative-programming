class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def perm(i,curr):
            if i==n:
                if len(curr)==n:
                    ans.append(curr[:])
                return
            visited = set()
            for m in nums:
                if m not in curr:
                    curr.append(m)
                    perm(i+1, curr)
                    curr.pop()
                    perm(i+1, curr)
        perm(0, [])
        return ans