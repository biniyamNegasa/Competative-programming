class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        n = len(nums)

        def com(i, curr):
            if i==n:
                ans.add(tuple(curr))
                return
            curr.append(nums[i])
            com(i+1, curr)
            curr.pop()
            com(i+1, curr)
        com(0, [])
        return ans