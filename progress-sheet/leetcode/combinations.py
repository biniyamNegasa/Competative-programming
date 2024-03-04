class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def com(i, k, curr):
            if len(curr)==k:
                ans.append(curr[:])
                return
            if i==n+1:
                return
            
            curr.append(i)
            com(i+1, k, curr)
            curr.pop()
            com(i+1, k, curr)
        com(1, k, [])
        return ans