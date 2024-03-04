class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def com(i, curr):
            if len(curr)==k and sum(curr)==n:
                ans.append(curr[:])
                return
            if i==10 or sum(curr)>n:
                return
            for j in range(i, 10):
                curr.append(j)
                com(j+1, curr)
                curr.pop()
        com(1,[])
        return ans