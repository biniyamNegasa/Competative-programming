class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(candidates)
        def com(i,t, curr, tot):
            if tot==t:
                ans.add(tuple(curr))
                return
            if i==n or tot>t:
                return
            curr.append(candidates[i])
            com(i+1, t, curr, tot+candidates[i])
            com(i, t, curr, tot+candidates[i])
            curr.pop()
            com(i+1, t, curr, tot)
        com(0, target, [], 0)
        return ans