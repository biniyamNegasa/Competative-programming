class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def com(i,curr, tar, tot):
            if tot==tar:
                ans.append(curr[:])
                return
            if tot>tar:
                return
            for j in range(i,n):    
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                curr.append(candidates[j])
                com(j+1, curr, tar, tot+candidates[j])
                curr.pop()
        com(0,[], target, 0)
        return ans